import json
import random

def create_train_val_test_splits():
    """Create 80/10/10 train/validation/test splits"""
    print("=== CREATING TRAIN/VAL/TEST SPLITS ===")
    
    # Load all examples
    examples = []
    with open('processed_data/complete_manual_dataset.jsonl', 'r') as f:
        for line in f:
            examples.append(json.loads(line.strip()))
    
    # Shuffle the examples
    random.seed(42)  # For reproducibility
    random.shuffle(examples)
    
    # Calculate split sizes
    total = len(examples)
    train_size = int(total * 0.8)
    val_size = int(total * 0.1)
    test_size = total - train_size - val_size
    
    print(f"Total examples: {total}")
    print(f"Train: {train_size} ({train_size/total*100:.1f}%)")
    print(f"Validation: {val_size} ({val_size/total*100:.1f}%)")
    print(f"Test: {test_size} ({test_size/total*100:.1f}%)")
    
    # Create splits
    train_examples = examples[:train_size]
    val_examples = examples[train_size:train_size + val_size]
    test_examples = examples[train_size + val_size:]
    
    # Save splits
    def save_split(examples, filename):
        with open(filename, 'w') as f:
            for example in examples:
                f.write(json.dumps(example) + '\n')
        print(f"✅ Saved {len(examples)} examples to {filename}")
    
    save_split(train_examples, 'processed_data/train.jsonl')
    save_split(val_examples, 'processed_data/validation.jsonl')
    save_split(test_examples, 'processed_data/test.jsonl')
    
    # Verify splits don't overlap
    train_inputs = set(ex['input'] for ex in train_examples)
    val_inputs = set(ex['input'] for ex in val_examples)
    test_inputs = set(ex['input'] for ex in test_examples)
    
    overlap_train_val = train_inputs & val_inputs
    overlap_train_test = train_inputs & test_inputs
    overlap_val_test = val_inputs & test_inputs
    
    print(f"\n=== OVERLAP CHECK ===")
    print(f"Train-Val overlap: {len(overlap_train_val)} examples")
    print(f"Train-Test overlap: {len(overlap_train_test)} examples")
    print(f"Val-Test overlap: {len(overlap_val_test)} examples")
    
    if len(overlap_train_val) > 0 or len(overlap_train_test) > 0 or len(overlap_val_test) > 0:
        print("⚠️  Warning: Found overlapping examples between splits!")
    else:
        print("✅ No overlapping examples found")
    
    return train_size, val_size, test_size

def analyze_emergency_distribution():
    """Analyze how emergency types are distributed across splits"""
    print("\n=== EMERGENCY TYPE DISTRIBUTION ===")
    
    def get_emergency_type(input_text):
        """Extract emergency type from input text"""
        input_lower = input_text.lower()
        
        # Medical emergencies
        if 'heat stroke' in input_lower or 'overheating' in input_lower:
            return 'heat_stroke'
        elif 'hypothermia' in input_lower or 'too cold' in input_lower or 'freezing' in input_lower:
            return 'hypothermia'
        elif 'allergic' in input_lower or 'anaphylaxis' in input_lower:
            return 'allergic_reaction'
        elif 'altitude' in input_lower or 'mountain sickness' in input_lower:
            return 'altitude_sickness'
        elif 'dehydrat' in input_lower or 'no water' in input_lower:
            return 'dehydration'
        elif 'tick' in input_lower:
            return 'tick_bite'
        elif 'sunburn' in input_lower or 'burned by sun' in input_lower:
            return 'sunburn'
        elif 'bee' in input_lower or 'wasp' in input_lower or 'sting' in input_lower:
            return 'bee_sting'
        elif 'snake' in input_lower:
            return 'snake_bite'
        elif 'seizure' in input_lower or 'convuls' in input_lower or 'epileptic' in input_lower:
            return 'seizure'
        elif 'faint' in input_lower or 'passed out' in input_lower or 'unconscious' in input_lower:
            return 'fainting'
        elif 'vertigo' in input_lower or 'dizz' in input_lower or 'spinning' in input_lower:
            return 'vertigo'
        elif 'eye' in input_lower:
            return 'eye_injury'
        elif 'nose' in input_lower and 'bleed' in input_lower:
            return 'nose_bleed'
        elif 'fever' in input_lower or 'temperature' in input_lower or 'burning up' in input_lower:
            return 'fever'
        elif 'bruise' in input_lower or 'black and blue' in input_lower or 'contusion' in input_lower:
            return 'bruises'
        elif 'sprain' in input_lower or 'twisted' in input_lower or 'sports injury' in input_lower:
            return 'sprains'
        elif 'fracture' in input_lower or 'broken' in input_lower or 'bone' in input_lower:
            return 'fractures'
        elif 'head' in input_lower and ('injury' in input_lower or 'trauma' in input_lower or 'wound' in input_lower):
            return 'head_injury'
        elif 'cut' in input_lower or 'bleeding cut' in input_lower:
            return 'cuts'
        elif 'chok' in input_lower or "can't breathe" in input_lower or 'blocked airway' in input_lower:
            return 'choking'
        elif 'cpr' in input_lower or 'cardiac' in input_lower or 'heart stopped' in input_lower or 'not breathing' in input_lower:
            return 'cpr'
        elif 'drown' in input_lower or 'underwater' in input_lower or 'water rescue' in input_lower:
            return 'drowning'
        else:
            return 'other'
    
    # Count emergency types across all data
    all_types = set()
    
    # Load splits and count types
    splits = {'train': [], 'validation': [], 'test': []}
    
    for split_name in splits.keys():
        with open(f'processed_data/{split_name}.jsonl', 'r') as f:
            for line in f:
                example = json.loads(line.strip())
                splits[split_name].append(example)
                all_types.add(get_emergency_type(example['input']))
    
    print(f"✅ Found {len(all_types)} different emergency types across all splits")
    print(f"Emergency types: {', '.join(sorted(all_types))}")

if __name__ == "__main__":
    # Create splits
    train_size, val_size, test_size = create_train_val_test_splits()
    
    # Analyze distribution
    analyze_emergency_distribution()
    
    print(f"\n=== PHASE 1 COMPLETE ===")
    print(f"✅ {train_size + val_size + test_size} total examples processed")
    print(f"✅ Train/Val/Test splits created")
    print(f"✅ Ready for Phase 2: Fine-tuning Gemma 3n") 