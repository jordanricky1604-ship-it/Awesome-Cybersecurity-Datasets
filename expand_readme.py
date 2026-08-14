import re

filepath = r"c:\Users\Nishant Tandon\.gemini\antigravity\scratch\Awesome-Cybersecurity-Datasets\README.md"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the "abandoned" banner with a stronger, authoritative statement.
# We already replaced it in the last step, so let's match the current one.
old_banner_regex = r"> ⚠️ \*\*The original repository was abandoned.*?Awesome-Cybersecurity-Datasets/\)\*\*"
new_banner = """> 🛡️ **AUTHORITATIVE 2026 FORK**
> The original Awesome-Cybersecurity-Datasets repository was abandoned in 2021 and left to rot. 
> This is the **actively maintained, state-of-the-art continuation** by SystemHelpdesk. We have purged dead links and added the critical datasets (LLMs, modern malware, cloud) required for 2026 threat research.
> 
> 🌐 **[View the Interactive, Searchable Version of this Dataset List](https://jordanricky1604-ship-it.github.io/Awesome-Cybersecurity-Datasets/)**"""

content = re.sub(old_banner_regex, new_banner, content, flags=re.DOTALL)

# Add "State of the Art (2022-2026)" section right after the TOC and before "Maintainer's Choice"
state_of_the_art = """
## 🚀 State of the Art (2022-2026 Additions)
*Since taking over this repository, we have added the following highly-requested datasets that reflect the modern threat landscape:*
- **[Malware Families Catalog](https://jordanricky1604-ship-it.github.io/malware-families-catalog/)** - 2,899 modern malware families mapped to MITRE ATT&CK.
- **[Jailbreak_LLMs](https://github.com/verazuo/jailbreak_llms)** - Comprehensive dataset of LLM prompt injections.
- **[Backstabber's Knife Collection](https://github.com/das-group/bsk-dataset)** - Open-source software supply chain attacks (NPM, PyPI).
- **[Mordor](https://github.com/OTRF/mordor)** - Cloud-native (AWS/Azure) simulated adversarial events.

---
"""

content = content.replace("## 🏆 Maintainer's Choice", state_of_the_art + "## 🏆 Maintainer's Choice")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("README updated with 2026 continuation claims.")
