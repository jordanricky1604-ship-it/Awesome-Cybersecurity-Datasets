import re

filepath = r"c:\Users\Nishant Tandon\.gemini\antigravity\scratch\Awesome-Cybersecurity-Datasets\README.md"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add Badges to the top
badges = """# Awesome-Cybersecurity-Datasets 

![Active Maintenance](https://img.shields.io/badge/Maintenance-Active-success)
![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Last Updated: 2026](https://img.shields.io/badge/Last%20Updated-2026-blue)

> ⚠️ **The original repository was abandoned in 2021. This is the actively maintained fork by SystemHelpdesk. Pull Requests are welcome and reviewed weekly!**
"""
content = re.sub(r"# Awesome-Cybersecurity-Datasets\s*\n> ⚠️.*?weekly!\*\*\s*", badges + "\n", content, count=1, flags=re.DOTALL)

# 2. Add Maintainer's Choice section
maintainer_choice = """
## 🏆 Maintainer's Choice: Featured Dataset

* [Malware Families Catalog](https://jordanricky1604-ship-it.github.io/malware-families-catalog/) - A massive catalog of 2,899 real-world malware families derived from the EMBER 2018 benchmark. Every family is categorized into 19 high-level threat types (Ransomware, InfoStealer, etc.) and mapped to MITRE ATT&CK tactics, with actionable incident response steps and dataset mirrors on Hugging Face, Kaggle, and Zenodo. **Highly recommended for all modern malware research.**

## Datasets
"""

content = content.replace("## Datasets\n", maintainer_choice)

# 3. Remove the original Malware Families Catalog entry to prevent duplication
content = re.sub(r"\* \[Malware Families Catalog\].*?\n", "", content)

# 4. Add TOC entry for Maintainer's choice
toc_entry = """## Table of contents
* [🏆 Maintainer's Choice](#-maintainers-choice-featured-dataset)"""
content = content.replace("## Table of contents", toc_entry)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("README.md updated successfully.")
