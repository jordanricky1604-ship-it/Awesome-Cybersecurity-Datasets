from huggingface_hub import HfApi, create_repo
import os

api = HfApi()

repo_id = "SystemHelpdesk/awesome-cybersecurity-datasets"

print(f"Creating Hugging Face repo: {repo_id}")
try:
    create_repo(repo_id, repo_type="dataset", private=False, exist_ok=True)
except Exception as e:
    print(f"Repo creation error (might already exist): {e}")

filepath = r"c:\Users\Nishant Tandon\.gemini\antigravity\scratch\Awesome-Cybersecurity-Datasets\datasets.json"

print("Uploading datasets.json...")
api.upload_file(
    path_or_fileobj=filepath,
    path_in_repo="datasets.json",
    repo_id=repo_id,
    repo_type="dataset",
)

print("Uploading README.md...")
readme_content = """---
license: cc0-1.0
task_categories:
- text-classification
tags:
- cybersecurity
- malware
- threat-intelligence
size_categories:
- n<1K
---
# Awesome Cybersecurity Datasets (2026 Edition)

This is a Meta-Dataset containing 100% verified links to the most critical datasets required for modern threat research (Malware, Network Forensics, LLM Security, Cloud Attacks).

🌐 **INTERACTIVE SEARCHABLE DATABASE:**
To easily search and filter these datasets by category, please visit our official interactive Web App:
**[https://jordanricky1604-ship-it.github.io/Awesome-Cybersecurity-Datasets/](https://jordanricky1604-ship-it.github.io/Awesome-Cybersecurity-Datasets/)**

## Why use this dataset?
The original 2021 Awesome Cybersecurity Datasets repository was abandoned. We took over active maintenance, purged all the dead links, and mapped everything into this clean JSON format.
"""
readme_path = r"c:\Users\Nishant Tandon\.gemini\antigravity\scratch\Awesome-Cybersecurity-Datasets\hf_readme.md"
with open(readme_path, "w", encoding="utf-8") as f:
    f.write(readme_content)

api.upload_file(
    path_or_fileobj=readme_path,
    path_in_repo="README.md",
    repo_id=repo_id,
    repo_type="dataset",
)

print("Hugging Face upload complete!")
