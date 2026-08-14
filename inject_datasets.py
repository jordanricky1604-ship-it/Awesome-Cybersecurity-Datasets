import json
import re

datasets_json_path = 'datasets.json'
readme_path = 'README.md'

new_datasets = [
    {
        "name": "LLM Jailbreak Dataset",
        "url": "https://huggingface.co/datasets/Necent/llm-jailbreak-prompt-injection-dataset",
        "description": "Hugging Face dataset featuring adversarial prompts and harmful content for testing LLM moderation.",
        "category": "Generative AI & LLM Security",
        "status": "active"
    },
    {
        "name": "Chatbot Prompt Injection",
        "url": "https://github.com/spml/chatbot-prompt-injection",
        "description": "Real-world system and user prompt interactions labeled for injection attempts.",
        "category": "Generative AI & LLM Security",
        "status": "active"
    },
    {
        "name": "Multimodal Prompt Injection",
        "url": "https://github.com/multimodal-security/multimodal-prompt-injection-dataset",
        "description": "Advanced attack vectors including agentic attacks and cross-modal delivery.",
        "category": "Generative AI & LLM Security",
        "status": "active"
    },
    {
        "name": "Kubernetes Dataset",
        "url": "https://github.com/yigitsever/kubernetes-dataset",
        "description": "Network flow data of CVE exploits and container escapes in K8s clusters.",
        "category": "Cloud & Container Security",
        "status": "active"
    },
    {
        "name": "Cloud Monitoring Dataset",
        "url": "https://github.com/microsoft/cloud-monitoring-dataset",
        "description": "Microsoft's massive cloud telemetry dataset for anomaly detection.",
        "category": "Cloud & Container Security",
        "status": "active"
    },
    {
        "name": "FORGE-Artifacts",
        "url": "https://github.com/shenyimings/FORGE-Artifacts",
        "description": "High-quality curated dataset of smart contract audits and vulnerabilities constructed via LLMs.",
        "category": "Web3 & Smart Contracts",
        "status": "active"
    },
    {
        "name": "Smart Contract Vuln Dataset",
        "url": "https://github.com/CoderDamien/smart-contract-vuln-dataset",
        "description": "Large-scale Solidity dataset with line-level annotations.",
        "category": "Web3 & Smart Contracts",
        "status": "active"
    },
    {
        "name": "SCV-List",
        "url": "https://github.com/sirhashalot/SCV-List",
        "description": "Focuses on advanced, unconventional vulnerabilities in DeFi protocols.",
        "category": "Web3 & Smart Contracts",
        "status": "active"
    },
    {
        "name": "Car-Hacking-Dataset",
        "url": "https://github.com/ocslab/car-hacking-dataset",
        "description": "Famous CAN bus intrusion detection dataset featuring DoS, fuzzy, and spoofing attacks.",
        "category": "Automotive & IoT Security",
        "status": "active"
    },
    {
        "name": "CIC Datasets",
        "url": "https://www.unb.ca/cic/datasets/",
        "description": "The Canadian Institute for Cybersecurity's robust collection of 2024+ PCAP and malware traffic.",
        "category": "Modern Malware Benchmarks",
        "status": "active"
    }
]

# Update JSON
with open(datasets_json_path, 'r', encoding='utf-8') as f:
    datasets = json.load(f)

datasets.extend(new_datasets)

with open(datasets_json_path, 'w', encoding='utf-8') as f:
    json.dump(datasets, f, indent=4)

print("Injected 10 datasets into datasets.json")

# Update README TOC
with open(readme_path, 'r', encoding='utf-8') as f:
    readme = f.read()

toc_target = "* [Governance, Risk, and Compliance (C-Suite)](#governance-risk-and-compliance-c-suite)"
toc_replacement = toc_target + "\n* [Web3 & Smart Contracts](#web3--smart-contracts)\n* [Automotive & IoT Security](#automotive--iot-security)"
readme = readme.replace(toc_target, toc_replacement)

# Update README Body Sections
# We will append the new categories at the end of the file.
new_categories = """
### Web3 & Smart Contracts
* [FORGE-Artifacts](https://github.com/shenyimings/FORGE-Artifacts) - High-quality curated dataset of smart contract audits and vulnerabilities constructed via LLMs.
* [Smart Contract Vuln Dataset](https://github.com/CoderDamien/smart-contract-vuln-dataset) - Large-scale Solidity dataset with line-level annotations.
* [SCV-List](https://github.com/sirhashalot/SCV-List) - Focuses on advanced, unconventional vulnerabilities in DeFi protocols.

### Automotive & IoT Security
* [Car-Hacking-Dataset](https://github.com/ocslab/car-hacking-dataset) - Famous CAN bus intrusion detection dataset featuring DoS, fuzzy, and spoofing attacks.
"""
readme += new_categories

# We also need to inject the items into existing categories:
# Generative AI & LLM Security
ai_target = "### Generative AI & LLM Security\n"
ai_inject = """* [LLM Jailbreak Dataset](https://huggingface.co/datasets/Necent/llm-jailbreak-prompt-injection-dataset) - Hugging Face dataset featuring adversarial prompts and harmful content for testing LLM moderation.
* [Chatbot Prompt Injection](https://github.com/spml/chatbot-prompt-injection) - Real-world system and user prompt interactions labeled for injection attempts.
* [Multimodal Prompt Injection](https://github.com/multimodal-security/multimodal-prompt-injection-dataset) - Advanced attack vectors including agentic attacks and cross-modal delivery.
"""
readme = readme.replace(ai_target, ai_target + ai_inject)

# Cloud & Container Security
cloud_target = "### Cloud & Container Security\n"
cloud_inject = """* [Kubernetes Dataset](https://github.com/yigitsever/kubernetes-dataset) - Network flow data of CVE exploits and container escapes in K8s clusters.
* [Cloud Monitoring Dataset](https://github.com/microsoft/cloud-monitoring-dataset) - Microsoft's massive cloud telemetry dataset for anomaly detection.
"""
readme = readme.replace(cloud_target, cloud_target + cloud_inject)

# Modern Malware Benchmarks
malware_target = "### Modern Malware Benchmarks\n"
malware_inject = """* [CIC Datasets](https://www.unb.ca/cic/datasets/) - The Canadian Institute for Cybersecurity's robust collection of 2024+ PCAP and malware traffic.
"""
readme = readme.replace(malware_target, malware_target + malware_inject)


with open(readme_path, 'w', encoding='utf-8') as f:
    f.write(readme)

print("Injected datasets into README.md")
