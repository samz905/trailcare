import json
import re
import random

def parse_response_to_steps(response_text, tag):
    """Parse a response text into structured steps"""
    # Clean up the response text
    response_text = response_text.strip()
    
    # Split by numbered patterns like "1)", "2)", etc.
    numbered_steps = re.split(r'(\d+\))', response_text)
    steps = []
    
    if len(numbered_steps) > 2:  # Has numbered steps
        step_num = 1
        for i in range(1, len(numbered_steps), 2):
            if i + 1 < len(numbered_steps):
                step_text = numbered_steps[i + 1].strip()
                if step_text:
                    # Extract title and description
                    title, description = extract_title_description(step_text, tag, step_num)
                    steps.append({
                        "step": step_num,
                        "title": title,
                        "description": description
                    })
                    step_num += 1
    else:
        # No numbered steps, try to split by sentences or logical breaks
        sentences = re.split(r'[.!?]+', response_text)
        sentences = [s.strip() for s in sentences if s.strip()]
        
        # Group sentences into logical steps
        if len(sentences) > 1:
            step_num = 1
            for sentence in sentences:
                if len(sentence) > 20:  # Only meaningful sentences
                    title, description = extract_title_description(sentence, tag, step_num)
                    steps.append({
                        "step": step_num,
                        "title": title,
                        "description": description
                    })
                    step_num += 1
        else:
            # Single long text, create one step
            title, description = extract_title_description(response_text, tag, 1)
            steps.append({
                "step": 1,
                "title": title,
                "description": description
            })
    
    return steps

def extract_title_description(text, tag, step_num):
    """Extract title and description from step text"""
    # Common action keywords for titles
    action_keywords = {
        'wash': 'Clean and Wash',
        'apply': 'Apply Treatment',
        'ice': 'Apply Ice',
        'pressure': 'Apply Pressure',
        'bandage': 'Bandage Wound',
        'rest': 'Rest and Elevate',
        'compress': 'Apply Compression',
        'elevate': 'Elevate Area',
        'drink': 'Stay Hydrated',
        'seek': 'Seek Medical Help',
        'call': 'Call for Help',
        'cpr': 'Perform CPR',
        'remove': 'Remove Object',
        'cover': 'Cover Area',
        'take': 'Take Medication',
        'avoid': 'Avoid Harmful Actions',
        'check': 'Check and Monitor',
        'position': 'Position Patient',
        'honey': 'Apply Natural Remedy',
        'ginger': 'Use Natural Treatment'
    }
    
    text = text.strip()
    first_sentence = text.split('.')[0].strip()
    
    # Try to find action keyword
    title = f"Step {step_num}"
    for keyword, action in action_keywords.items():
        if keyword.lower() in first_sentence.lower():
            title = action
            break
    
    # If no keyword found, try to extract from first few words
    if title == f"Step {step_num}":
        words = first_sentence.split()[:3]
        if words:
            title = ' '.join(words).title()
    
    return title, text

def create_training_examples():
    """Create training examples from the valid intents"""
    print("=== CONVERTING TO STRUCTURED JSON ===")
    
    # Load the intents
    with open('raw_data/intents.json', 'r') as f:
        data = json.load(f)
    
    intents = data['intents']
    
    # Filter valid intents (non-empty responses)
    valid_intents = [intent for intent in intents if intent['responses'] and intent['responses'] != [" "]]
    
    print(f"Processing {len(valid_intents)} valid intents...")
    
    training_examples = []
    
    for intent in valid_intents:
        tag = intent['tag']
        patterns = intent['patterns']
        response = intent['responses'][0]  # Take first response
        
        # Convert response to structured steps
        steps = parse_response_to_steps(response, tag)
        
        # Create training examples for each pattern
        for pattern in patterns:
            example = {
                "input": pattern,
                "output": {
                    "steps": steps
                }
            }
            training_examples.append(example)
    
    print(f"Created {len(training_examples)} training examples")
    
    # Show sample examples
    print("\n=== SAMPLE EXAMPLES ===")
    for i, example in enumerate(training_examples[:3]):
        print(f"\nExample {i+1}:")
        print(f"Input: {example['input']}")
        print(f"Steps: {len(example['output']['steps'])}")
        for step in example['output']['steps']:
            print(f"  {step['step']}. {step['title']}: {step['description'][:50]}...")
    
    return training_examples

def save_as_jsonl(examples, filename):
    """Save examples as JSONL format"""
    with open(filename, 'w') as f:
        for example in examples:
            f.write(json.dumps(example) + '\n')
    print(f"✅ Saved {len(examples)} examples to {filename}")

if __name__ == "__main__":
    # Create training examples
    examples = create_training_examples()
    
    # Save as JSONL
    save_as_jsonl(examples, 'processed_data/training_examples.jsonl')
    
    print(f"\n✅ Successfully processed {len(examples)} training examples!")
    print("📁 Saved to: processed_data/training_examples.jsonl") 