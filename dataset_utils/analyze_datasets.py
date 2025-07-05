import json
import pandas as pd
from datasets import load_dataset

def analyze_intents_dataset():
    """Analyze the Kaggle intents.json dataset"""
    print("=== ANALYZING INTENTS.JSON (KAGGLE) ===")
    
    # Load the dataset
    with open('raw_data/intents.json', 'r') as f:
        data = json.load(f)
    
    intents = data['intents']
    
    print(f"Total number of intents: {len(intents)}")
    print(f"Structure: {list(intents[0].keys())}")
    
    # Analyze each field
    tags = [intent['tag'] for intent in intents]
    print(f"\nUnique tags: {len(set(tags))}")
    print("Tags:", tags[:10], "..." if len(tags) > 10 else "")
    
    # Check for empty responses
    empty_responses = [intent for intent in intents if not intent['responses'] or intent['responses'] == [" "]]
    print(f"\nIntents with empty responses: {len(empty_responses)}")
    if empty_responses:
        print("Empty response tags:", [intent['tag'] for intent in empty_responses])
    
    # Pattern analysis
    total_patterns = sum(len(intent['patterns']) for intent in intents)
    print(f"\nTotal patterns: {total_patterns}")
    print("Sample patterns:", intents[0]['patterns'])
    
    # Response analysis
    valid_responses = [intent for intent in intents if intent['responses'] and intent['responses'] != [" "]]
    print(f"\nIntents with valid responses: {len(valid_responses)}")
    print("Sample response:", valid_responses[0]['responses'][0][:100] + "..." if len(valid_responses[0]['responses'][0]) > 100 else valid_responses[0]['responses'][0])
    
    return intents

def load_huggingface_dataset():
    """Load the HuggingFace dataset"""
    print("\n=== LOADING HUGGINGFACE DATASET ===")
    
    try:
        ds = load_dataset("badri55/First_aid__dataset")
        print("Dataset loaded successfully!")
        print(f"Dataset keys: {list(ds.keys())}")
        
        # Check if it's a train/test split or just one dataset
        for split_name, split_data in ds.items():
            print(f"\n{split_name} split:")
            print(f"  Number of samples: {len(split_data)}")
            print(f"  Features: {list(split_data.features.keys())}")
            
            # Show first few samples
            if len(split_data) > 0:
                sample = split_data[0]
                print(f"  Sample data: {sample}")
                
        return ds
        
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None

if __name__ == "__main__":
    # Analyze both datasets
    intents_data = analyze_intents_dataset()
    huggingface_data = load_huggingface_dataset()
    
    print("\n=== SUMMARY ===")
    print("✅ Intents.json: Loaded and analyzed")
    print("✅ HuggingFace dataset: Attempting to load...") 