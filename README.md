# Awesome Cybersecurity Datasets [![Awesome](https://awesome.re/badge.svg)](https://github.com/sindresorhus/awesome)



> 🛡️ **AUTHORITATIVE 2026 FORK**
> The original Awesome-Cybersecurity-Datasets repository was abandoned in 2021 and left to rot. 
> This is the **actively maintained, state-of-the-art continuation** by SystemHelpdesk. We have purged dead links and added the critical datasets (LLMs, modern malware, cloud) required for 2026 threat research.
> 
> 🌐 **[View the Interactive, Searchable Version](https://jordanricky1604-ship-it.github.io/Awesome-Cybersecurity-Datasets/)**
> 🤗 **[Hugging Face Dataset Mirror](https://huggingface.co/Jordan123234)**
> 📊 **[Kaggle Dataset Mirror](https://www.kaggle.com/rickyjordan)**
> 📝 **[Dev.to Technical Guides](https://dev.to/jordanricky1604-ship-it)**

A curated list of amazingly awesome Cybersecurity datasets. 

Please contribute to this list with new datasets by sending me a pull request.

Happy learning!

## Contents
- [🏆 Maintainer's Choice: Featured Dataset](#-maintainers-choice-featured-dataset)
- [Datasets](#datasets)
  - [Network traffic](#network-traffic)
  - [Malware](#malware)
  - [Software](#software)
  - [WebApps](#webapps)
  - [URLs & Domain Names](#urls--domain-names)
  - [Host](#host)
  - [Email](#email)
  - [Fraud](#fraud)
  - [Honeypots](#honeypots)
  - [Binaries](#binaries)
  - [Phishing](#phishing)
  - [Passwords](#passwords)
  - [MISC](#misc)
  - [Generative AI & LLM Security](#generative-ai--llm-security)
  - [Modern Malware Benchmarks](#modern-malware-benchmarks)
  - [Cloud & Container Security](#cloud--container-security)
  - [Software Supply Chain](#software-supply-chain)
  - [Governance, Risk, and Compliance (C-Suite)](#governance-risk-and-compliance-c-suite)
  - [Web3 & Smart Contracts](#web3--smart-contracts)
  - [Automotive & IoT Security](#automotive--iot-security)
  - [Threat Intelligence & Vulnerability Data](#threat-intelligence--vulnerability-data)
  - [ICS & Critical Infrastructure Security](#ics--critical-infrastructure-security)
  - [Deepfake & Synthetic Media Detection](#deepfake--synthetic-media-detection)





## 🏆 Maintainer's Choice: Featured Dataset


## Datasets
### Network traffic
- [DEF CON CTF Network Traffic](https://www.defcon.org/html/links/dc-torrent.html) - Full PCAP network traffic from DEF CON Capture The Flag competitions. Incredible for analyzing zero-day exploits and active red-team vs. blue-team network warfare.
- [AWID (Aegean WiFi Intrusion Dataset)](http://icsdweb.aegean.gr/awid/) - The most comprehensive public dataset specifically dedicated to wireless network intrusions. Contains millions of labeled 802.11 MAC layer frames capturing WEP/WPA cracking, rogue APs, etc.
- [Comprehensive, Multi-Source Cyber-Security Events](https://csr.lanl.gov/data/cyber1/) - This data set represents 58 consecutive days of de-identified event data collected from five sources within Los Alamos National Laboratory's corporate, internal computer network.
- [User-Computer Authentication Associations in Time](https://csr.lanl.gov/data/auth/) - This anonymized data set encompasses 9 continuous months and represents 708,304,516 successful authentication events from users to computers collected from the Los Alamos National Laboratory (LANL) enterprise network.
- [Canadian Institute for Cybersecurity datasets](https://www.unb.ca/cic/datasets/index.html) - Used around the world by universities, private industry and independent researchers.
- [KDD Cup 1999 Data](http://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html) - This database contains a standard set of data to be audited, which includes a wide variety of intrusions simulated in a military network environment.
- [NSL-KDD Dataset](https://www.unb.ca/cic/datasets/nsl.html) - Often viewed as the "corrected" version of the original KDD Cup 1999 dataset. It removes the massive number of duplicate records found in the original, providing a more rigorous benchmark.
- [2017-SUEE-data-set](https://github.com/vs-uulm/2017-SUEE-data-set) - The data sets contain traffic in and out of the web server of the Student Union for Electrical Engineering (Fachbereichsvertretung Elektrotechnik) at Ulm University. Internal hosts are hosts from within the university network, some of them are cable bound, others connect through one of two wifi services on campus (eduroam and welcome). The data was mixed with attack traffic.
- [CTU-13 Dataset](https://www.stratosphereips.org/datasets-ctu13/) - A Labeled Dataset with Botnet, Normal and Background traffic.
- [PCAP files](https://www.netresec.com/index.ashx?page=PcapFiles) - Malware Traffic, Network Forensics, SCADA/ICS Network Captures, Packet Injection Attacks / Man-on-the-Side Attacks...
- [pcapt](https://www.pcapr.net) - Big repository of PCAP files.
- [Project Sonar](https://github.com/rapid7/sonar/wiki/UDP) - Produces multiple UDP datasets every month. This data is gathered by sending protocol-specific UDP probes across the entire IPv4 address space. The types of probes sent each week continues to expand as the project matures.

### Malware
- [AndroZoo](https://androzoo.uni.lu/) - The absolute gold standard for mobile security research. Contains over 20 million Android applications (APKs) sourced from multiple markets, analyzed by dozens of anti-virus products.
- [UNSW-NB15 data set](https://www.unsw.adfa.edu.au/unsw-canberra-cyber/cybersecurity/ADFA-NB15-Datasets/) - This data set has nine families of attacks, namely, Fuzzers, Analysis, Backdoors, DoS, Exploits, Generic, Reconnaissance, Shellcode and Worms. The Argus, Bro-IDS tools are utilised and twelve algorithms are developed to generate totally 49 features with the class label.
- [Malware Training Sets](https://marcoramilli.blogspot.com/2016/12/malware-training-sets-machine-learning.html) - Today (please refers to blog post date) the collected classified datasets is composed by the following samples: APT1 292 Samples, Crypto 2024 Samples, Locker 434 Samples, Zeus 2014 Samples.
- [The Drebin Dataset](https://www.sec.cs.tu-bs.de/~danarp/drebin/) - The dataset contains 5,560 applications from 179 different malware families. The samples have been collected in the period of August 2010 to October 2012 and were made available to us by the MobileSandbox project.
- [Stratosphere IPS](https://www.stratosphereips.org/datasets-overview/) - Malware captures, Normal captures, mixed captures...
- [Microsoft Malware Classification Challenge](https://www.kaggle.com/c/malware-classification/data) - You are provided with a set of known malware files representing a mix of 9 different families. Each malware file has an Id, a 20 character hash value uniquely identifying the file, and a Class, an integer representing one of 9 family names.

### Software
- [JavaScript Vulnerability dataset](http://www.inf.u-szeged.hu/~ferenc/papers/JSVulnerabilityDataSet/)  - Dataset constructed from the vulnerability information in public databases of the Node Security Project and the Snyk platform, and code fixing patches from GitHub.

### WebApps
- [Web Attack Payloads](https://github.com/foospidy/payloads) - A collection of web attack payloads.
- [Machine-Learning-driven-Web-Application-Firewall](https://github.com/faizann24/Fwaf-Machine-Learning-driven-Web-Application-Firewall) - Set of good and bad queries to a web application firewall.
- [Internet-Wide Scan Data Repository](https://scans.io/) - The Censys Projects publishes daily snapshots of what we know about each IPv4 host, Alexa Top Million website, and known X.509 certificate. These datasets contain structured, non-ephemeral JSON records that identify a host's configuration.
- [500K HTTP Headers](https://hackertarget.com/500k-http-headers/) - Recently we crawled the Top 500K sites (as ranked by Alexa). Following requests from readers we are making available the HTTP Headers for research purposes.
- [HTTP DATASET CSIC 2010](http://web.archive.org/web/20130924222653/http://iec.csic.es/dataset) - The HTTP dataset CSIC 2010 contains thousands of web requests automatically generated. It can be used for the testing of web attack protection systems. It was developed at the Information Security Institute of CSIC (Spanish Research National Council).
- [OpenAppSec WAF Comparison Dataset](https://github.com/openappsec/openappsec) - A modern dataset of millions of requests and tens of thousands of malicious payloads explicitly designed to test modern WAF evasion techniques.
- [30-Day ModSecurity Production Dataset](https://github.com/hslatman/awesome-industrial-control-system-security) - Real malicious HTTP requests blocked by the OWASP ModSecurity Core Rule Set (CRS) on a live production server.
- [Common Crawl](http://commoncrawl.org/the-data/get-started/) - The Common Crawl corpus contains petabytes of data collected over the last 7 years. It contains raw web page data, extracted metadata and text extractions.
- [AZSecure-data](https://www.azsecure-data.org/get-data.html) - The AZSecure-data PORTAL currently provides access to Web forums, Internet phishing websites, Twitter data, and other data.

### URLs & Domain Names
- [Malicious URLs Dataset](http://www.sysnet.ucsd.edu/projects/url/) - The data set consists of about 2.4 million URLs (examples) and 3.2 million features.
- [Feodo Tracker](https://feodotracker.abuse.ch/) - List of Feodo botnet C&C servers.
- [URLhaus](https://urlhaus.abuse.ch/api/) - A project from abuse.ch with the goal of sharing malicious URLs that are being used for malware distribution.
- [Alexa Top 1 Million](http://s3.amazonaws.com/alexa-static/top-1m.csv.zip) - CSV dataset with the most popular sites by Alexa.
- [Tranco List](https://tranco-list.eu/) - The modern academic standard replacing Alexa. It provides a hardened, daily-updated ranking by aggregating Cloudflare, Chrome UX, and other sources to prevent manipulation.
- [Cloudflare Radar Domain Rankings](https://radar.cloudflare.com/domains) - Based on live 1.1.1.1 resolver data, highly relevant for modern traffic popularity.
- [OpenDNS Top Domains List](https://github.com/opendns/public-domain-lists) - The OpenDNS Top Domains List is the top 10,000 domain names our resolvers all over the globe are receiving queries for, sorted by popularity.
- [StopForumSpam](https://www.stopforumspam.com/downloads) - The data provided here represents what we believe will only ever ben used to abuse. IP Addresses, domains and usernames listed here will be returned in API results as "blacklisted".

### Host
- [The ADFA Intrusion Detection Datasets](https://www.unsw.adfa.edu.au/unsw-canberra-cyber/cybersecurity/ADFA-IDS-Datasets/) - This dataset provides a contemporary Linux dataset for evaluation by traditional HIDS. This dataset provides a contemporary Windows dataset for evaluation by HIDS.
- [Public Security Log Sharing Site](http://log-sharing.dreamhosters.com/) - This site contains various free shareable log samples from various systems, security and network devices, applications, etc. The logs are collected from real systems, some contain evidence of compromise and other malicious activity. Wherever possible, the logs are NOT sanitized, anonymized or modified in any way (just as they came from the logging system).
- [Aktaion2 Data](https://github.com/jzadeh/aktaion2/tree/master/data) - The project is meant to be a learning/teaching tool on how to blend multiple security signals and behaviors into an expressive framework for intrusion detection.

### Email
- [The Enron Email Corpus](http://www.cs.cmu.edu/~enron/) - The absolute foundation for digital forensics, e-discovery, and insider-threat detection. Contains half a million emails from Enron executives prior to the company's collapse.

### Fraud
- [Credit Card Fraud](https://www.kaggle.com/samkirkiles/credit-card-fraud/data) - The datasets contains transactions made by credit cards in September 2013 by european cardholders. This dataset presents transactions that occurred in two days, where we have 492 frauds out of 284,807 transactions. The dataset is highly unbalanced, the positive class (frauds) account for 0.172% of all transactions.

### Honeypots
- [DDS Dataset Collection](http://datadrivensecurity.info/blog/pages/dds-dataset-collection.html) - A tar/gzip CSV file from a collection of AWS honeypots. A zip CSV file of domains and a high level classification of dga or legit along with a subclass of either legit, cryptolocker, gox or newgoz.
- [Threat_Research](https://github.com/JonathanPhillips/Threat_Research) - Centralized repository to dump threat research data gathered from my network of honeypots.

### Binaries
- [The ember dataset](https://github.com/endgameinc/ember) - A collection of 1.1 million sha256 hashes from PE files that were scanned sometime in 2017. This repository makes it easy to reproducibly train the benchmark model, extend the provided feature set, or classify new PE files with the benchmark model.

### Phishing
- [Phishing Websites Data Set](https://archive.ics.uci.edu/ml/datasets/phishing+websites#) - In this dataset, we shed light on the important features that have proved to be sound and effective in predicting phishing websites. In addition, we propose some new features.

### Passwords
- [Yahoo Password Frequency Corpus](https://figshare.com/articles/Yahoo_Password_Frequency_Corpus/2057937) - This dataset includes sanitized password frequency lists collected from Yahoo in May 2011.
- [RockYou2024](https://github.com/danielmiessler/SecLists) - A massive compilation of nearly 10 billion plaintext credentials aggregated from thousands of recent data breaches. It is the absolute standard for penetration testing wordlists.
- [Have I Been Pwned (Pwned Passwords)](https://haveibeenpwned.com/Passwords) - The industry-standard k-anonymity dataset for checking breached credentials securely without exposing passwords.

### MISC
- [SecRepo](http://www.secrepo.com/) - Samples of Security Related Data.


### Generative AI & LLM Security
- [Tencent/AI-Infra-Guard](https://github.com/Tencent/AI-Infra-Guard) - A full-stack AI red teaming platform including modern LLM jailbreak evaluation datasets, agent security scanning, and vulnerability assessments (Updated 2026).
- [JailbreakBench](https://github.com/JailbreakBench/JailbreakBench) - The industry-standard repository for tracking state-of-the-art LLM jailbreaks and defenses. Features a continuously updated dataset of adversarial prompts.
- [LLM Jailbreak Taxonomy & Simulation](https://github.com/zakky8/llm-jailbreak-taxonomy) - Contains a taxonomy of 40 modern adversarial attack patterns, experiment notebooks, and simulation harnesses calibrated to 2025-2026 attack success rates.
- [Jailbreak_LLMs](https://github.com/verazuo/jailbreak_llms) - A massive, highly-cited dataset of 15,140 prompts in the wild, including 1,405 specifically categorized as jailbreak prompts.
- [Awesome-Jailbreak-on-LLMs](https://github.com/jelliezhong/Awesome-Jailbreak-on-LLMs) - An actively maintained, curated list of research papers, defense frameworks, and detection methods for modern LLMs.
- [CIC-SBAN Datasets 2025](https://www.unb.ca/cic/datasets/#sban-2025) - A modern dataset from the Canadian Institute for Cybersecurity focusing specifically on Large Language Model (LLM) security, prompt injection payloads, and model extraction attacks.

### Modern Malware Benchmarks
- [EMBER2024](https://github.com/elastic/ember) - Released in 2025, this is a massive update to the original EMBER benchmark. It includes metadata, labels, and features for over 3.2 million files across six formats, specifically designed for training ML models against modern evasive malware.
- [SOREL-20M](https://github.com/sophos/SOREL-20M) - The Sophos-ReversingLabs 20 Million dataset. Released in late 2020, this is the modern benchmark for training PE malware detection models.
- [Malware Families Catalog](https://jordanricky1604-ship-it.github.io/malware-families-catalog) - A structured dataset of 2,900+ curated malware families with MITRE ATT&CK mapping and hunting queries. Available in JSONL and Parquet.
- [BODMAS](https://whyisyoung.github.io/BODMAS/) - Blue Hexagon Open Dataset for Malware Analysis. Features timestamped malware samples and behavioral vectors for temporal drift analysis.

### Cloud & Container Security
- [Kubernetes Dataset](https://github.com/yigitsever/kubernetes-dataset) - Network flow data of CVE exploits and container escapes in Kubernetes clusters.
- [Cloud Monitoring Dataset](https://github.com/microsoft/cloud-monitoring-dataset) - Microsoft's massive cloud telemetry dataset for anomaly detection.
- [Mordor](https://github.com/OTRF/mordor) - The Mordor project provides pre-recorded, high-quality security events (JSON) generated by simulated adversarial techniques, heavily featuring cloud environments (AWS/Azure).
- [Flaws.cloud Logs](http://flaws.cloud/) - Log datasets from the famous AWS security challenges, providing real-world CloudTrail and S3 access logs of cloud compromise.

### Software Supply Chain
- [Backstabber's Knife Collection](https://github.com/das-group/bsk-dataset) - A curated dataset of open-source software supply chain attacks, containing malicious packages collected from NPM, PyPI, and RubyGems.


### Governance, Risk, and Compliance (C-Suite)
- [VERIS Community Database (VCDB)](https://github.com/vz-risk/VCDB) - A public, open-source repository of security incidents documented using the VERIS framework. This dataset powers the annual Verizon Data Breach Investigations Report (DBIR) and is critical for enterprise risk modeling.
- [CERT Insider Threat Dataset](https://resources.sei.cmu.edu/library/asset-view.cfm?assetid=508099) - Synthetic logs of simulated malicious insider behavior within sociotechnical networks, developed by Carnegie Mellon University (SEI) for User Behavior Analytics (UBA) and insider threat training.

### Web3 & Smart Contracts
- [FORGE-Artifacts](https://github.com/shenyimings/FORGE-Artifacts) - High-quality curated dataset of smart contract audits and vulnerabilities constructed via LLMs.
- [Smart Contract Vuln Dataset](https://github.com/CoderDamien/smart-contract-vuln-dataset) - Large-scale Solidity dataset with line-level annotations.
- [SCV-List](https://github.com/sirhashalot/SCV-List) - Focuses on advanced, unconventional vulnerabilities in DeFi protocols.

### Automotive & IoT Security
- [IoT-23 Dataset](https://www.stratosphereips.org/datasets-iot23) - A massive benchmark consisting of 20 malicious PCAP captures of real IoT malware (like Mirai and Torii) executing on actual IoT hardware, plus 3 benign captures.
- [CIC-YNU-IoTMal 2026](https://www.unb.ca/cic/datasets/iotmal-2026.html) - A state-of-the-art IoT malware dataset capturing network traffic and host-based telemetry for emerging IoT threats in edge environments.
- [Car-Hacking-Dataset](https://github.com/ocslab/car-hacking-dataset) - Famous CAN bus intrusion detection dataset featuring DoS, fuzzy, and spoofing attacks.

### Threat Intelligence & Vulnerability Data
- [CISA Known Exploited Vulnerabilities (KEV) Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) - The authoritative, constantly updated dataset of CVEs that carry active, real-world exploitation evidence. Essential for vulnerability prioritization research.
- [Cybersecurity Attacks & Defense Dataset 2026](https://www.kaggle.com/datasets) - A curated Kaggle dataset aggregating real-world threat data from 2024–2026, including malicious domains, IPs, and CVE exploit patterns.

### ICS & Critical Infrastructure Security
- [HAI (HIL-based Augmented ICS) Security Dataset](https://github.com/icsdataset/hai) - Industrial control system operational data collected from a testbed augmented with Hardware-In-the-Loop (HIL) simulators. Contains multiple attack scenarios.
- [WUSTL-IIOT Dataset](https://www.cse.wustl.edu/~jain/iiot/) - A dataset specifically built to emulate real-world industrial systems, focusing on reconnaissance attacks and network scanning in ICS testbeds.
- [ICS-Security-Tools/pcaps](https://github.com/ICS-Security-Tools/pcaps) - A massive repository containing a wide variety of PCAP files specifically for ICS/SCADA network traffic, including DNP3, Profinet, and Siemens S7Comm.

### Deepfake & Synthetic Media Detection
- [DeepfakeBench](https://github.com/SCLBD/DeepfakeBench) - A comprehensive benchmark dataset containing state-of-the-art (SOTA) image and video detection methods for standardized evaluation.
- [FaceForensics++](https://github.com/ondyari/FaceForensics) - One of the most common datasets, consisting of 1,000 original videos manipulated using Deepfakes, Face2Face, FaceSwap, and NeuralTextures.
- [Celeb-DF (v2)](https://github.com/yuezunli/celeb-deepfakeforensics) - A large-scale, high-quality dataset containing 590 real videos and 5,639 deepfake videos, known for being extremely challenging due to high visual quality.
