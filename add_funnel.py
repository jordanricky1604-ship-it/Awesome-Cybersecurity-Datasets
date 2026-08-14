import re

filepath = r"c:\Users\Nishant Tandon\.gemini\antigravity\scratch\Awesome-Cybersecurity-Datasets\README.md"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Add link to GitHub Pages site to funnel authority
funnel_link = """
> ⚠️ **The original repository was abandoned in 2021. This is the actively maintained fork by SystemHelpdesk. Pull Requests are welcome and reviewed weekly!**
> 
> 🌐 **[View the Interactive Version of this Dataset List](https://jordanricky1604-ship-it.github.io/Awesome-Cybersecurity-Datasets/)**
"""

content = content.replace("> ⚠️ **The original repository was abandoned in 2021. This is the actively maintained fork by SystemHelpdesk. Pull Requests are welcome and reviewed weekly!**\n", funnel_link)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Funnel link added.")
