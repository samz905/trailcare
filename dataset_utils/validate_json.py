import json
import statistics

def validate_training_examples():
    """Validate the generated training examples"""
    print("=== VALIDATING TRAINING EXAMPLES ===")
    
    # Load the training examples
    examples = []
    with open('processed_data/training_examples.jsonl', 'r') as f:
        for line in f:
            examples.append(json.loads(line.strip()))
    
    print(f"Total examples: {len(examples)}")
    
    # Validation checks
    valid_count = 0
    errors = []
    
    step_counts = []
    title_lengths = []
    description_lengths = []
    
    for i, example in enumerate(examples):
        try:
            # Check structure
            if 'input' not in example or 'output' not in example:
                errors.append(f"Example {i}: Missing 'input' or 'output' field")
                continue
            
            if 'steps' not in example['output']:
                errors.append(f"Example {i}: Missing 'steps' in output")
                continue
            
            steps = example['output']['steps']
            step_counts.append(len(steps))
            
            # Check each step
            for j, step in enumerate(steps):
                if 'step' not in step or 'title' not in step or 'description' not in step:
                    errors.append(f"Example {i}, Step {j}: Missing required fields")
                    continue
                
                # Check step numbering
                if step['step'] != j + 1:
                    errors.append(f"Example {i}, Step {j}: Step number should be {j+1}, got {step['step']}")
                
                # Track metrics
                title_lengths.append(len(step['title']))
                description_lengths.append(len(step['description']))
                
                # Check for meaningless titles
                if step['title'].startswith('Step ') or len(step['title']) < 3:
                    errors.append(f"Example {i}, Step {j}: Generic or too short title: '{step['title']}'")
                
                # Check for too short descriptions
                if len(step['description']) < 10:
                    errors.append(f"Example {i}, Step {j}: Description too short: '{step['description']}'")
            
            valid_count += 1
            
        except Exception as e:
            errors.append(f"Example {i}: Error processing - {str(e)}")
    
    # Print results
    print(f"\n=== VALIDATION RESULTS ===")
    print(f"✅ Valid examples: {valid_count}/{len(examples)}")
    print(f"❌ Errors found: {len(errors)}")
    
    if errors:
        print("\n⚠️  First 10 errors:")
        for error in errors[:10]:
            print(f"  - {error}")
        if len(errors) > 10:
            print(f"  ... and {len(errors) - 10} more")
    
    # Statistics
    print(f"\n=== STATISTICS ===")
    print(f"Steps per example: {statistics.mean(step_counts):.1f} (range: {min(step_counts)}-{max(step_counts)})")
    print(f"Title length: {statistics.mean(title_lengths):.1f} chars (range: {min(title_lengths)}-{max(title_lengths)})")
    print(f"Description length: {statistics.mean(description_lengths):.1f} chars (range: {min(description_lengths)}-{max(description_lengths)})")
    
    # Sample good examples
    print(f"\n=== SAMPLE GOOD EXAMPLES ===")
    good_examples = [ex for ex in examples if len(ex['output']['steps']) >= 3][:2]
    for i, example in enumerate(good_examples):
        print(f"\nExample {i+1}:")
        print(f"Input: {example['input']}")
        print(f"Steps ({len(example['output']['steps'])}):")
        for step in example['output']['steps']:
            print(f"  {step['step']}. {step['title']}: {step['description'][:60]}...")
    
    return len(errors) == 0

def count_unique_scenarios():
    """Count unique emergency scenarios"""
    print("\n=== EMERGENCY SCENARIO COVERAGE ===")
    
    examples = []
    with open('processed_data/training_examples.jsonl', 'r') as f:
        for line in f:
            examples.append(json.loads(line.strip()))
    
    # Extract unique inputs to see coverage
    unique_inputs = set()
    emergency_types = set()
    
    for example in examples:
        unique_inputs.add(example['input'].lower())
        # Try to extract emergency type from input
        input_lower = example['input'].lower()
        if 'cut' in input_lower:
            emergency_types.add('cuts')
        elif 'sprain' in input_lower:
            emergency_types.add('sprains')
        elif 'fever' in input_lower:
            emergency_types.add('fever')
        elif 'bite' in input_lower:
            emergency_types.add('bites')
        elif 'fracture' in input_lower:
            emergency_types.add('fractures')
        elif 'cpr' in input_lower:
            emergency_types.add('cpr')
        elif 'chok' in input_lower:
            emergency_types.add('choking')
        elif 'burn' in input_lower:
            emergency_types.add('burns')
        elif 'drown' in input_lower:
            emergency_types.add('drowning')
        # Add more as needed...
    
    print(f"Unique input patterns: {len(unique_inputs)}")
    print(f"Emergency types covered: {len(emergency_types)}")
    print(f"Emergency types: {sorted(emergency_types)}")
    
    return len(emergency_types)

if __name__ == "__main__":
    # Run validation
    is_valid = validate_training_examples()
    
    # Count coverage
    coverage = count_unique_scenarios()
    
    print(f"\n=== FINAL STATUS ===")
    print(f"✅ JSON format: {'VALID' if is_valid else 'INVALID'}")
    print(f"✅ Emergency coverage: {coverage} types")
    print(f"✅ Ready for fine-tuning: {'YES' if is_valid and coverage > 10 else 'NO'}") 