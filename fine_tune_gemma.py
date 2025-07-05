#!/usr/bin/env python3
"""
Fine-tune Gemma 3n for Emergency First Aid using Unsloth
Enhanced with detailed logging and checkpoint management
"""

import json
import os
import torch
from pathlib import Path
from typing import Dict, List, Any
import logging
from datetime import datetime

# Import Unsloth and related libraries
from unsloth import FastLanguageModel
from datasets import Dataset
from transformers import TrainingArguments, TrainerCallback
from trl import SFTTrainer

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('fine_tuning.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Constants
MODEL_NAME = "unsloth/gemma-2-2b-bnb-4bit"  # Base Gemma 2B model
MAX_SEQ_LENGTH = 2048
LOAD_IN_4BIT = True

# LoRA Configuration
LORA_R = 16
LORA_ALPHA = 16
LORA_DROPOUT = 0
TARGET_MODULES = ["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"]

# Training Configuration
OUTPUT_DIR = "./gemma_emergency_fine_tuned"
EPOCHS = 3
BATCH_SIZE = 2
GRADIENT_ACCUMULATION_STEPS = 4
LEARNING_RATE = 2e-4
WARMUP_STEPS = 5
LOGGING_STEPS = 1
SAVE_STEPS = 25  # Save checkpoints every 25 steps
EVAL_STEPS = 25  # Evaluate every 25 steps

class DetailedLoggingCallback(TrainerCallback):
    """Custom callback for detailed logging during training"""
    
    def on_train_begin(self, args, state, control, **kwargs):
        logger.info("🚀 Starting fine-tuning process...")
        logger.info(f"📊 Training configuration:")
        logger.info(f"   - Epochs: {EPOCHS}")
        logger.info(f"   - Batch size: {BATCH_SIZE}")
        logger.info(f"   - Learning rate: {LEARNING_RATE}")
        logger.info(f"   - LoRA rank: {LORA_R}")
        logger.info(f"   - Max sequence length: {MAX_SEQ_LENGTH}")
        logger.info(f"   - Output directory: {OUTPUT_DIR}")
        
    def on_step_end(self, args, state, control, **kwargs):
        if state.global_step % LOGGING_STEPS == 0:
            logger.info(f"📈 Step {state.global_step}: Training in progress...")
            
    def on_save(self, args, state, control, **kwargs):
        logger.info(f"💾 Checkpoint saved at step {state.global_step}")
        
    def on_evaluate(self, args, state, control, **kwargs):
        logger.info(f"📊 Evaluation completed at step {state.global_step}")
        
    def on_train_end(self, args, state, control, **kwargs):
        logger.info("🎉 Training completed successfully!")

def load_dataset(file_path: str) -> List[Dict[str, Any]]:
    """Load the emergency dataset from JSONL file."""
    logger.info(f"Loading dataset from {file_path}")
    data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            data.append(json.loads(line.strip()))
    logger.info(f"Loaded {len(data)} samples")
    return data

def create_prompt_template(input_text: str, output_data: Dict[str, Any] = None) -> str:
    """
    Create the prompt template for first aid expert responses.
    
    Format:
    ### Instruction:
    You're a first aid expert. Based on the emergency described, generate step-by-step JSON instructions with fields: step, title, and description.
    
    ### Input:
    {emergency_description}
    
    ### Response:
    {json_output}
    """
    
    prompt = f"""### Instruction:
You're a first aid expert. Based on the emergency described, generate step-by-step JSON instructions with fields: step, title, and description.

### Input:
{input_text}

### Response:
"""
    
    if output_data:
        # Format the output as a clean JSON string
        response_json = json.dumps(output_data, indent=2)
        prompt += response_json
    
    return prompt

def prepare_training_data(data: List[Dict[str, Any]]) -> Dataset:
    """Prepare the training data in the format expected by SFTTrainer."""
    logger.info("Preparing training data...")
    formatted_data = []
    
    for i, item in enumerate(data):
        input_text = item["input"]
        output_data = item["output"]
        
        # Create the full prompt with both input and expected output
        full_prompt = create_prompt_template(input_text, output_data)
        
        formatted_data.append({
            "text": full_prompt
        })
        
        if i < 3:  # Log first 3 examples
            logger.info(f"Example {i+1} prompt length: {len(full_prompt)} characters")
    
    logger.info(f"Prepared {len(formatted_data)} training examples")
    return Dataset.from_list(formatted_data)

def setup_model_and_tokenizer():
    """Set up the model and tokenizer with Unsloth."""
    logger.info("Loading model and tokenizer...")
    
    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name=MODEL_NAME,
        max_seq_length=MAX_SEQ_LENGTH,
        dtype=None,  # Auto-detect
        load_in_4bit=LOAD_IN_4BIT,
    )
    
    logger.info("Setting up LoRA adaptation...")
    model = FastLanguageModel.get_peft_model(
        model,
        r=LORA_R,
        target_modules=TARGET_MODULES,
        lora_alpha=LORA_ALPHA,
        lora_dropout=LORA_DROPOUT,
        bias="none",
        use_gradient_checkpointing="unsloth",
        random_state=3407,
        use_rslora=False,
        loftq_config=None,
    )
    
    logger.info("Model and tokenizer setup complete")
    return model, tokenizer

def train_model(model, tokenizer, train_dataset: Dataset, val_dataset: Dataset = None):
    """Train the model using SFTTrainer."""
    logger.info("Initializing training...")
    
    # Create output directory if it doesn't exist
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    training_args = TrainingArguments(
        output_dir=OUTPUT_DIR,
        num_train_epochs=EPOCHS,
        per_device_train_batch_size=BATCH_SIZE,
        per_device_eval_batch_size=BATCH_SIZE,
        gradient_accumulation_steps=GRADIENT_ACCUMULATION_STEPS,
        learning_rate=LEARNING_RATE,
        warmup_steps=WARMUP_STEPS,
        logging_steps=LOGGING_STEPS,
        save_steps=SAVE_STEPS,
        evaluation_strategy="steps" if val_dataset else "no",
        eval_steps=EVAL_STEPS if val_dataset else None,
        save_strategy="steps",
        load_best_model_at_end=True if val_dataset else False,
        metric_for_best_model="eval_loss" if val_dataset else None,
        greater_is_better=False,
        report_to="none",  # Disable wandb logging
        remove_unused_columns=False,
        dataloader_pin_memory=False,
        save_total_limit=5,  # Keep only 5 recent checkpoints
        logging_dir=f"{OUTPUT_DIR}/logs",
    )
    
    trainer = SFTTrainer(
        model=model,
        tokenizer=tokenizer,
        train_dataset=train_dataset,
        eval_dataset=val_dataset,
        args=training_args,
        dataset_text_field="text",
        max_seq_length=MAX_SEQ_LENGTH,
        callbacks=[DetailedLoggingCallback()],
    )
    
    logger.info("Starting training process...")
    logger.info(f"Total training steps: {len(train_dataset) * EPOCHS // (BATCH_SIZE * GRADIENT_ACCUMULATION_STEPS)}")
    
    # Train the model
    trainer.train()
    
    # Save the final model
    logger.info("Saving final model...")
    trainer.save_model()
    
    logger.info("Training completed successfully!")
    return trainer

def test_model(model, tokenizer, test_cases: List[str]):
    """Test the fine-tuned model with sample inputs."""
    logger.info("Testing fine-tuned model...")
    
    FastLanguageModel.for_inference(model)  # Enable native 2x faster inference
    
    for i, test_input in enumerate(test_cases, 1):
        logger.info(f"Testing case {i}: {test_input[:50]}...")
        
        # Create prompt for inference
        prompt = create_prompt_template(test_input)
        
        # Generate response
        inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
        
        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_new_tokens=512,
                temperature=0.7,
                do_sample=True,
                pad_token_id=tokenizer.eos_token_id
            )
        
        # Decode response
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        # Extract only the generated part (after the prompt)
        generated_part = response[len(prompt):].strip()
        
        logger.info(f"Generated response for case {i}: {generated_part[:100]}...")
        
        # Try to parse as JSON
        try:
            json.loads(generated_part)
            logger.info(f"✅ Case {i}: Valid JSON generated")
        except json.JSONDecodeError:
            logger.warning(f"⚠️ Case {i}: Invalid JSON format")

def main():
    """Main fine-tuning pipeline."""
    logger.info("🚑 EMERGENCY FIRST AID FINE-TUNING")
    logger.info("=" * 50)
    
    # Load datasets
    train_data = load_dataset("processed_data/train.jsonl")
    val_data = load_dataset("processed_data/validation.jsonl")
    
    # Prepare training data
    train_dataset = prepare_training_data(train_data)
    val_dataset = prepare_training_data(val_data)
    
    # Setup model and tokenizer
    model, tokenizer = setup_model_and_tokenizer()
    
    # Train the model
    trainer = train_model(model, tokenizer, train_dataset, val_dataset)
    
    # Test with sample cases
    test_cases = [
        "I have a deep cut on my arm that's bleeding heavily.",
        "Someone is choking on food and can't breathe.",
        "My friend fell and hit their head, they're unconscious.",
        "I got burned by hot oil while cooking.",
        "Someone is having chest pain and difficulty breathing."
    ]
    
    test_model(model, tokenizer, test_cases)
    
    logger.info("Fine-tuning pipeline completed successfully!")
    logger.info(f"Model saved to: {OUTPUT_DIR}")

if __name__ == "__main__":
    main() 