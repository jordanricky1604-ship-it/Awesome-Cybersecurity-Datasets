import re
import json

filepath = r"c:\Users\Nishant Tandon\.gemini\antigravity\scratch\Awesome-Cybersecurity-Datasets\README.md"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

datasets = []
current_category = None

lines = content.split('\n')
for line in lines:
    line = line.strip()
    # Check for categories (### Category Name)
    if line.startswith('### '):
        current_category = line[4:].strip()
    
    # Also check the State of the Art section which has unordered list
    elif line.startswith('## 🚀 State of the Art'):
        current_category = "State of the Art (2026)"
        
    # Match dataset entries: * [Name](url) - Description or - **[Name](url)** - Description
    elif line.startswith('* [') or line.startswith('- **['):
        # Match standard: * [Name](URL) - Description
        # Match SOTA: - **[Name](URL)** - Description
        match = re.search(r'\[([^\]]+)\]\(([^)]+)\)[*]*\s*-\s*(.*)', line)
        if match:
            name = match.group(1).strip()
            url = match.group(2).strip()
            desc = match.group(3).strip()
            category = current_category if current_category else "Uncategorized"
            datasets.append({
                "name": name,
                "url": url,
                "description": desc,
                "category": category,
                "status": "pending_check"
            })

with open(r"c:\Users\Nishant Tandon\.gemini\antigravity\scratch\Awesome-Cybersecurity-Datasets\datasets.json", 'w', encoding='utf-8') as f:
    json.dump(datasets, f, indent=4)

print(f"Extracted {len(datasets)} datasets.")
