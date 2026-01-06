import json
import os

def transform_mapping():
    file_path = 'file_mapping.json'
    
    # Read existing mapping
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    new_data = []
    
    # Process mmlu
    if 'mmlu' in data:
        for filename, zh_desc in data['mmlu'].items():
            # Generate English description from filename
            # abstract_algebra_test.json -> Abstract Algebra
            base_name = filename.replace('_test.json', '')
            en_desc = base_name.replace('_', ' ').title()
            
            new_data.append({
                "zh": zh_desc,
                "en": en_desc,
                "file": filename,
                "type": "mmlu"
            })
            
    # Process mmlu-pro
    if 'mmlu-pro' in data:
        for filename, zh_desc in data['mmlu-pro'].items():
            # Generate English description from filename
            # biology.json -> Biology
            base_name = filename.replace('.json', '')
            en_desc = base_name.replace('_', ' ').title()
            
            new_data.append({
                "zh": zh_desc,
                "en": en_desc,
                "file": filename,
                "type": "mmlu-pro"
            })
    
    # Write back to file
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(new_data, f, ensure_ascii=False, indent=2)
    
    print(f"Successfully transformed {len(new_data)} entries.")

if __name__ == "__main__":
    transform_mapping()
