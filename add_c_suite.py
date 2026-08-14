import os

with open('README.md', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Table of Contents
toc_addition = "* [Governance, Risk, and Compliance (C-Suite)](#governance-risk-and-compliance-c-suite)\n"
content = content.replace('* [Software Supply Chain](#software-supply-chain)', '* [Software Supply Chain](#software-supply-chain)\n' + toc_addition)

# 2. Append new datasets
datasets_addition = """

### Governance, Risk, and Compliance (C-Suite)
* [VERIS Community Database (VCDB)](https://github.com/vz-risk/VCDB) - A public, open-source repository of security incidents documented using the VERIS framework. This dataset powers the annual Verizon Data Breach Investigations Report (DBIR) and is critical for enterprise risk modeling.
* [CERT Insider Threat Dataset](https://resources.sei.cmu.edu/library/asset-view.cfm?assetid=508099) - Synthetic logs of simulated malicious insider behavior within sociotechnical networks, developed by Carnegie Mellon University (SEI) for User Behavior Analytics (UBA) and insider threat training.
"""

content = content + datasets_addition

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(content)

print('README.md updated successfully with C-Suite datasets.')
