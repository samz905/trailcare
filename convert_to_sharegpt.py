import json

input_path = 'processed_data/complete_manual_dataset.jsonl'
output_path = 'processed_data/complete_manual_dataset_sharegpt.jsonl'

with open(input_path, 'r', encoding='utf-8') as infile, open(output_path, 'w', encoding='utf-8') as outfile:
    for line in infile:
        line = line.strip()
        if not line:
            continue
        data = json.loads(line)
        user_input = data['input']
        # Compact JSON, no newlines or extra spaces
        assistant_output = json.dumps(data['output'], ensure_ascii=False, separators=(',', ':'))
        sharegpt_entry = {
            'conversations': [
                {'content': user_input, 'role': 'user'},
                {'content': assistant_output, 'role': 'assistant'}
            ],
            'source': 'manual-first-aid',
            'score': 0.8
        }
        outfile.write(json.dumps(sharegpt_entry, ensure_ascii=False) + '\n')