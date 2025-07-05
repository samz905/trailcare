#!/usr/bin/env python3
"""
Convert fine-tuned Gemma model to GGUF format for Ollama integration
"""

import os
import subprocess
import shutil
from pathlib import Path
from unsloth import FastLanguageModel

# Configuration
FINE_TUNED_MODEL_PATH = "./gemma_emergency_fine_tuned"
OUTPUT_DIR = "./gemma_emergency_gguf"
OLLAMA_MODEL_NAME = "gemma-emergency-aid"

def check_dependencies():
    """Check if required tools are available."""
    print("🔍 Checking dependencies...")
    
    # Check if llama.cpp is available
    try:
        result = subprocess.run(["which", "llama-convert"], capture_output=True, text=True)
        if result.returncode != 0:
            print("❌ llama.cpp not found. Please install it first:")
            print("   git clone https://github.com/ggerganov/llama.cpp")
            print("   cd llama.cpp && make")
            print("   # Add llama.cpp to your PATH")
            return False
    except Exception:
        print("❌ Error checking for llama.cpp. Make sure it's installed and in PATH.")
        return False
    
    print("✅ Dependencies check passed")
    return True

def save_model_for_conversion():
    """Save the fine-tuned model in a format suitable for conversion."""
    print("💾 Preparing model for conversion...")
    
    if not Path(FINE_TUNED_MODEL_PATH).exists():
        print(f"❌ Fine-tuned model not found at: {FINE_TUNED_MODEL_PATH}")
        print("💡 Run fine_tune_gemma.py first to create the model.")
        return False
    
    try:
        # Load the fine-tuned model
        model, tokenizer = FastLanguageModel.from_pretrained(
            model_name=FINE_TUNED_MODEL_PATH,
            max_seq_length=2048,
            dtype=None,
            load_in_4bit=False,  # Use full precision for conversion
        )
        
        # Create output directory
        conversion_dir = Path(OUTPUT_DIR) / "hf_model"
        conversion_dir.mkdir(parents=True, exist_ok=True)
        
        # Save in HuggingFace format
        print(f"📁 Saving model to: {conversion_dir}")
        model.save_pretrained(str(conversion_dir))
        tokenizer.save_pretrained(str(conversion_dir))
        
        print("✅ Model prepared for conversion")
        return True
        
    except Exception as e:
        print(f"❌ Error preparing model: {e}")
        return False

def convert_to_gguf():
    """Convert the model to GGUF format using llama.cpp."""
    print("🔄 Converting to GGUF format...")
    
    hf_model_path = Path(OUTPUT_DIR) / "hf_model"
    gguf_output_path = Path(OUTPUT_DIR) / "gemma-emergency-aid.gguf"
    
    try:
        # Convert to GGUF
        cmd = [
            "llama-convert",
            str(hf_model_path),
            "--outfile", str(gguf_output_path),
            "--outtype", "f16"  # Use 16-bit precision
        ]
        
        print(f"Running: {' '.join(cmd)}")
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode != 0:
            print(f"❌ Conversion failed: {result.stderr}")
            return False
        
        print("✅ Conversion to GGUF completed")
        return True
        
    except Exception as e:
        print(f"❌ Error during conversion: {e}")
        return False

def create_ollama_modelfile():
    """Create Ollama Modelfile for the emergency aid model."""
    print("📝 Creating Ollama Modelfile...")
    
    gguf_path = Path(OUTPUT_DIR) / "gemma-emergency-aid.gguf"
    if not gguf_path.exists():
        print("❌ GGUF file not found")
        return False
    
    # Create Modelfile content
    modelfile_content = f'''FROM {gguf_path.absolute()}

TEMPLATE """### Instruction:
You're a first aid expert. Based on the emergency described, generate step-by-step JSON instructions with fields: step, title, and description.

### Input:
{{{{ .Prompt }}}}

### Response:
"""

PARAMETER temperature 0.3
PARAMETER top_p 0.9
PARAMETER stop "### Input:"
PARAMETER stop "### Instruction:"

SYSTEM """You are an expert first aid responder specializing in emergency situations for hikers and outdoor enthusiasts. You provide clear, actionable, step-by-step instructions in JSON format. Always respond with proper JSON containing a "steps" array where each step has "step" (number), "title" (brief action), and "description" (detailed instructions)."""
'''
    
    # Save Modelfile
    modelfile_path = Path(OUTPUT_DIR) / "Modelfile"
    with open(modelfile_path, 'w', encoding='utf-8') as f:
        f.write(modelfile_content)
    
    print(f"✅ Modelfile created: {modelfile_path}")
    return True

def create_ollama_model():
    """Create the Ollama model from the Modelfile."""
    print("🚀 Creating Ollama model...")
    
    modelfile_path = Path(OUTPUT_DIR) / "Modelfile"
    if not modelfile_path.exists():
        print("❌ Modelfile not found")
        return False
    
    try:
        # Change to the output directory
        original_cwd = os.getcwd()
        os.chdir(OUTPUT_DIR)
        
        # Create Ollama model
        cmd = ["ollama", "create", OLLAMA_MODEL_NAME, "-f", "Modelfile"]
        print(f"Running: {' '.join(cmd)}")
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        # Return to original directory
        os.chdir(original_cwd)
        
        if result.returncode != 0:
            print(f"❌ Failed to create Ollama model: {result.stderr}")
            return False
        
        print(f"✅ Ollama model '{OLLAMA_MODEL_NAME}' created successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Error creating Ollama model: {e}")
        return False

def test_ollama_model():
    """Test the created Ollama model with a sample emergency."""
    print("🧪 Testing Ollama model...")
    
    test_prompt = "I'm hiking and my friend is choking on some food. They can't speak or cough."
    
    try:
        cmd = ["ollama", "run", OLLAMA_MODEL_NAME, test_prompt]
        print(f"Test prompt: {test_prompt}")
        print("Response:")
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(result.stdout)
            print("✅ Model test completed")
            return True
        else:
            print(f"❌ Model test failed: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ Error testing model: {e}")
        return False

def create_usage_script():
    """Create a usage script for the Ollama model."""
    script_content = f'''#!/usr/bin/env python3
"""
Emergency First Aid Assistant - Ollama Integration
Usage script for the fine-tuned Gemma emergency aid model
"""

import subprocess
import json
import sys

MODEL_NAME = "{OLLAMA_MODEL_NAME}"

def get_emergency_help(emergency_description: str) -> str:
    """Get emergency first aid instructions using the fine-tuned model."""
    try:
        cmd = ["ollama", "run", MODEL_NAME, emergency_description]
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            return f"Error: {{result.stderr}}"
    except Exception as e:
        return f"Error running model: {{e}}"

def main():
    """Interactive emergency aid assistant."""
    print("🏥 Emergency First Aid Assistant")
    print("="*50)
    print("Describe your emergency situation and get step-by-step first aid instructions.")
    print("Type 'quit' to exit.\\n")
    
    while True:
        try:
            emergency = input("🚨 Describe the emergency: ").strip()
            
            if emergency.lower() in ['quit', 'exit', 'q']:
                print("Stay safe! 🏥")
                break
            
            if not emergency:
                continue
            
            print("\\n🔄 Getting first aid instructions...")
            response = get_emergency_help(emergency)
            
            print("\\n📋 First Aid Instructions:")
            print("-" * 30)
            print(response)
            print("-" * 30)
            print()
            
        except KeyboardInterrupt:
            print("\\n\\nStay safe! 🏥")
            break
        except Exception as e:
            print(f"Error: {{e}}")

if __name__ == "__main__":
    # Check if model exists
    try:
        result = subprocess.run(["ollama", "list"], capture_output=True, text=True)
        if MODEL_NAME not in result.stdout:
            print(f"❌ Model '{{MODEL_NAME}}' not found in Ollama.")
            print("💡 Run convert_to_ollama.py to create the model first.")
            sys.exit(1)
    except Exception:
        print("❌ Ollama not found. Please install Ollama first.")
        sys.exit(1)
    
    main()
'''
    
    script_path = Path("emergency_aid_assistant.py")
    with open(script_path, 'w', encoding='utf-8') as f:
        f.write(script_content)
    
    # Make it executable
    os.chmod(script_path, 0o755)
    
    print(f"✅ Usage script created: {script_path}")

def main():
    """Main conversion pipeline."""
    print("🔄 Converting Fine-tuned Model to Ollama Format")
    print("="*60)
    
    # Check dependencies
    if not check_dependencies():
        return
    
    # Step 1: Save model for conversion
    if not save_model_for_conversion():
        return
    
    # Step 2: Convert to GGUF
    if not convert_to_gguf():
        return
    
    # Step 3: Create Ollama Modelfile
    if not create_ollama_modelfile():
        return
    
    # Step 4: Create Ollama model
    if not create_ollama_model():
        return
    
    # Step 5: Test the model
    test_ollama_model()
    
    # Step 6: Create usage script
    create_usage_script()
    
    print("\\n🎉 Conversion completed successfully!")
    print(f"📱 Your emergency aid model is now available as: {OLLAMA_MODEL_NAME}")
    print("\\n🚀 Usage:")
    print(f"   ollama run {OLLAMA_MODEL_NAME} 'describe your emergency'")
    print("   python emergency_aid_assistant.py  # Interactive mode")

if __name__ == "__main__":
    main() 