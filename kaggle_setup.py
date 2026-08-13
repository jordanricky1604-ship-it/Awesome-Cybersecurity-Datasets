import os
import json
import shutil
import subprocess

export_dir = "kaggle_export"
os.makedirs(export_dir, exist_ok=True)

# Copy datasets.json
shutil.copy(
    "datasets.json",
    os.path.join(export_dir, "datasets.json")
)

# Create dataset-metadata.json
metadata = {
  "title": "Awesome Cybersecurity Datasets (2026)",
  "id": "jordanricky1604shipit/awesome-cybersecurity-datasets",
  "licenses": [
    {
      "name": "CC0-1.0"
    }
  ]
}

with open(os.path.join(export_dir, "dataset-metadata.json"), "w") as f:
    json.dump(metadata, f, indent=4)

# Create a README with the SEO backlink
readme_content = """# Awesome Cybersecurity Datasets (2026 Edition)

This is a Meta-Dataset containing 100% verified links to the most critical datasets required for modern threat research (Malware, Network Forensics, LLM Security, Cloud Attacks).

🌐 **INTERACTIVE SEARCHABLE DATABASE:**
To easily search and filter these datasets by category, please visit our official interactive Web App:
**[https://jordanricky1604-ship-it.github.io/Awesome-Cybersecurity-Datasets/](https://jordanricky1604-ship-it.github.io/Awesome-Cybersecurity-Datasets/)**

## Why use this dataset?
The original 2021 Awesome Cybersecurity Datasets repository was abandoned. We took over active maintenance, purged all the dead links, and mapped everything into this clean JSON format.

## Structure
`datasets.json` contains:
- `name`: Dataset Name
- `url`: Validated URL
- `category`: Assigned Security Category
- `description`: 1-2 sentence overview
"""
with open(os.path.join(export_dir, "README.md"), "w", encoding="utf-8") as f:
    f.write(readme_content)

print("Kaggle export directory prepared.")
