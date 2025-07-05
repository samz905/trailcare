#!/usr/bin/env python3
"""
Validate the fine-tuned Gemma model for JSON format and relevance
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Any, Tuple
from unsloth import FastLanguageModel
import torch

# Configuration
MODEL_PATH = "./gemma_emergency_fine_tuned"
MAX_SEQ_LENGTH = 2048
TEST_DATA_PATH = "processed_data/test.jsonl"

def load_test_data(file_path: str) -> List[Dict[str, Any]]:
    """Load test data from JSONL file."""
    data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            data.append(json.loads(line.strip()))
    return data

def create_prompt_template(input_text: str) -> str:
    """Create the prompt template for inference."""
    return f"""### Instruction:
You're a first aid expert. Based on the emergency described, generate step-by-step JSON instructions with fields: step, title, and description.

### Input:
{input_text}

### Response:
"""

def extract_json_from_response(response: str) -> Tuple[Dict[str, Any], bool]:
    """
    Extract JSON from model response and validate format.
    Returns (parsed_json, is_valid)
    """
    try:
        # Try to find JSON in the response
        # Look for content between { and }
        json_match = re.search(r'\{.*\}', response, re.DOTALL)
        if json_match:
            json_str = json_match.group()
            parsed_json = json.loads(json_str)
            return parsed_json, True
        else:
            return {}, False
    except json.JSONDecodeError:
        return {}, False

def validate_json_structure(parsed_json: Dict[str, Any]) -> Dict[str, bool]:
    """
    Validate that the JSON has the correct structure for emergency steps.
    Expected format:
    {
        "steps": [
            {
                "step": 1,
                "title": "Title",
                "description": "Description"
            }
        ]
    }
    """
    validation_results = {
        "has_steps_field": False,
        "steps_is_list": False,
        "all_steps_have_required_fields": False,
        "step_numbers_sequential": False,
        "reasonable_step_count": False
    }
    
    # Check if 'steps' field exists
    if "steps" in parsed_json:
        validation_results["has_steps_field"] = True
        steps = parsed_json["steps"]
        
        # Check if steps is a list
        if isinstance(steps, list):
            validation_results["steps_is_list"] = True
            
            # Check if all steps have required fields
            required_fields = ["step", "title", "description"]
            all_have_fields = all(
                isinstance(step, dict) and all(field in step for field in required_fields)
                for step in steps
            )
            validation_results["all_steps_have_required_fields"] = all_have_fields
            
            # Check if step numbers are sequential
            if steps and all_have_fields:
                step_numbers = [step.get("step") for step in steps]
                expected_numbers = list(range(1, len(steps) + 1))
                validation_results["step_numbers_sequential"] = step_numbers == expected_numbers
            
            # Check if reasonable number of steps (1-10)
            validation_results["reasonable_step_count"] = 1 <= len(steps) <= 10
    
    return validation_results

def evaluate_relevance(input_text: str, generated_steps: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Evaluate the relevance of generated steps to the input emergency.
    This is a simplified heuristic-based evaluation.
    """
    input_lower = input_text.lower()
    
    # Extract key emergency terms from input
    emergency_keywords = {
        "bleeding": ["blood", "bleeding", "cut", "wound"],
        "breathing": ["breath", "choking", "airway", "oxygen"],
        "burns": ["burn", "fire", "heat", "scald"],
        "fracture": ["fracture", "broken", "bone", "arm", "leg"],
        "cardiac": ["heart", "chest", "cardiac", "pulse"],
        "allergic": ["allergy", "allergic", "reaction", "swelling"],
        "head": ["head", "skull", "brain", "concussion"],
        "hypothermia": ["cold", "hypothermia", "freezing", "shivering"],
        "heat": ["heat", "hot", "fever", "temperature"],
        "drowning": ["water", "drown", "underwater"],
        "poison": ["poison", "snake", "bite", "venom"]
    }
    
    # Identify emergency type
    detected_emergency = None
    for emergency_type, keywords in emergency_keywords.items():
        if any(keyword in input_lower for keyword in keywords):
            detected_emergency = emergency_type
            break
    
    # Check if generated steps contain relevant terms
    all_step_text = " ".join([
        f"{step.get('title', '')} {step.get('description', '')}"
        for step in generated_steps
    ]).lower()
    
    relevance_score = 0
    if detected_emergency and detected_emergency in emergency_keywords:
        relevant_keywords = emergency_keywords[detected_emergency]
        matches = sum(1 for keyword in relevant_keywords if keyword in all_step_text)
        relevance_score = min(matches / len(relevant_keywords), 1.0)
    
    # Check for general first aid relevance
    general_first_aid_terms = [
        "call 911", "emergency", "medical", "hospital", "help", "pressure", 
        "apply", "check", "monitor", "position", "seek"
    ]
    general_matches = sum(1 for term in general_first_aid_terms if term in all_step_text)
    general_relevance = min(general_matches / 5, 1.0)  # Normalize to 0-1
    
    return {
        "detected_emergency": detected_emergency,
        "specific_relevance_score": relevance_score,
        "general_relevance_score": general_relevance,
        "overall_relevance": (relevance_score + general_relevance) / 2
    }

def load_model_for_inference():
    """Load the fine-tuned model for inference."""
    print("Loading fine-tuned model...")
    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name=MODEL_PATH,
        max_seq_length=MAX_SEQ_LENGTH,
        dtype=None,
        load_in_4bit=True,
    )
    FastLanguageModel.for_inference(model)  # Enable faster inference
    return model, tokenizer

def validate_single_example(model, tokenizer, input_text: str, expected_output: Dict[str, Any]) -> Dict[str, Any]:
    """Validate a single test example."""
    # Generate response
    prompt = create_prompt_template(input_text)
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=512,
            temperature=0.3,  # Lower temperature for more consistent output
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id
        )
    
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    generated_part = response[len(prompt):].strip()
    
    # Parse and validate JSON
    parsed_json, is_valid_json = extract_json_from_response(generated_part)
    
    validation_results = {}
    relevance_results = {}
    
    if is_valid_json:
        validation_results = validate_json_structure(parsed_json)
        if "steps" in parsed_json:
            relevance_results = evaluate_relevance(input_text, parsed_json["steps"])
    
    return {
        "input": input_text,
        "generated_response": generated_part,
        "parsed_json": parsed_json,
        "is_valid_json": is_valid_json,
        "validation_results": validation_results,
        "relevance_results": relevance_results,
        "expected_output": expected_output
    }

def main():
    """Main validation pipeline."""
    print("🔍 Validating Fine-tuned Emergency First Aid Model")
    print("="*60)
    
    # Check if model exists
    if not Path(MODEL_PATH).exists():
        print(f"❌ Fine-tuned model not found at: {MODEL_PATH}")
        print("💡 Run fine_tune_gemma.py first to create the model.")
        return
    
    # Check if test data exists
    if not Path(TEST_DATA_PATH).exists():
        print(f"❌ Test data not found at: {TEST_DATA_PATH}")
        return
    
    # Load test data
    print(f"📁 Loading test data from {TEST_DATA_PATH}")
    test_data = load_test_data(TEST_DATA_PATH)
    print(f"✅ Loaded {len(test_data)} test samples")
    
    # Load model
    model, tokenizer = load_model_for_inference()
    
    # Validate each test example
    print("\n🧪 Running validation tests...")
    results = []
    
    for i, test_item in enumerate(test_data, 1):
        print(f"Testing example {i}/{len(test_data)}: {test_item['input'][:50]}...")
        
        result = validate_single_example(
            model, tokenizer, 
            test_item["input"], 
            test_item["output"]
        )
        results.append(result)
    
    # Calculate overall statistics
    print("\n" + "="*60)
    print("📊 VALIDATION RESULTS")
    print("="*60)
    
    total_examples = len(results)
    valid_json_count = sum(1 for r in results if r["is_valid_json"])
    
    # JSON Format Statistics
    print(f"\n📋 JSON Format Validation:")
    print(f"  Valid JSON: {valid_json_count}/{total_examples} ({valid_json_count/total_examples*100:.1f}%)")
    
    if valid_json_count > 0:
        valid_results = [r for r in results if r["is_valid_json"]]
        
        validation_stats = {}
        for key in ["has_steps_field", "steps_is_list", "all_steps_have_required_fields", 
                   "step_numbers_sequential", "reasonable_step_count"]:
            count = sum(1 for r in valid_results if r["validation_results"].get(key, False))
            validation_stats[key] = count
            print(f"  {key.replace('_', ' ').title()}: {count}/{valid_json_count} ({count/valid_json_count*100:.1f}%)")
    
    # Relevance Statistics
    relevant_results = [r for r in results if r["is_valid_json"] and r["relevance_results"]]
    if relevant_results:
        avg_overall_relevance = sum(r["relevance_results"]["overall_relevance"] for r in relevant_results) / len(relevant_results)
        avg_specific_relevance = sum(r["relevance_results"]["specific_relevance_score"] for r in relevant_results) / len(relevant_results)
        avg_general_relevance = sum(r["relevance_results"]["general_relevance_score"] for r in relevant_results) / len(relevant_results)
        
        print(f"\n🎯 Relevance Evaluation:")
        print(f"  Overall Relevance: {avg_overall_relevance:.2f}/1.0")
        print(f"  Specific Relevance: {avg_specific_relevance:.2f}/1.0")
        print(f"  General First Aid Relevance: {avg_general_relevance:.2f}/1.0")
    
    # Show some examples
    print(f"\n📝 Sample Results:")
    for i, result in enumerate(results[:3], 1):
        print(f"\n--- Example {i} ---")
        print(f"Input: {result['input'][:100]}...")
        print(f"Valid JSON: {result['is_valid_json']}")
        if result['is_valid_json'] and result['relevance_results']:
            print(f"Relevance: {result['relevance_results']['overall_relevance']:.2f}")
        print(f"Generated: {result['generated_response'][:200]}...")
    
    # Save detailed results
    results_file = Path("validation_results.json")
    with open(results_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n💾 Detailed results saved to: {results_file}")
    
    # Overall assessment
    if valid_json_count / total_examples >= 0.8 and avg_overall_relevance >= 0.7:
        print("\n✅ Model validation PASSED! Ready for deployment.")
    else:
        print("\n⚠️  Model validation needs improvement. Consider additional training.")

if __name__ == "__main__":
    main() 