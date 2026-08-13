# Awesome-Cybersecurity-Datasets 
> ⚠️ **The original repository was abandoned in 2021. This is the actively maintained fork by SystemHelpdesk. Pull Requests are welcome and reviewed weekly!**

A curated list of amazingly awesome Cybersecurity datasets. 

Please contribute to this list with new datasets by sending me a pull request.

Happy learning!

## Table of contents
* [Network traffic](#network-traffic)
* [Malware](#malware)
* [WebApps](#webapps)
* [Software](#software)
* [URLs & Domain Names](#urls--domain-names)
* [Host](#host)
* [Email](#email)
* [Fraud](#fraud)
* [Honeypots](#honeypots)
* [Binaries](#binaries)
* [Phishing](#phising)
* [Passwords](#passwords)
* [MISC](#misc)
* [Generative AI & LLM Security](#generative-ai--llm-security)
* [Modern Malware Benchmarks](#modern-malware-benchmarks)
* [Cloud & Container Security](#cloud--container-security)
* [Software Supply Chain](#software-supply-chain)


## Datasets
### Network traffic
* [Unified Host and Network Dataset](https://csr.lanl.gov/data/2017.html) - The Unified Host and Network Dataset is a subset of network and computer (host) events collected from the Los Alamos National Laboratory enterprise network over the course of approximately 90 days. The host event logs originated from most enterprise computers running the Microsoft Windows operating system on Los Alamos National Laboratory's (LANL) enterprise network. The network event data originated from many of the internal enterprise routers within the LANL enterprise network.
* [Comprehensive, Multi-Source Cyber-Security Events](https://csr.lanl.gov/data/cyber1/) - This data set represents 58 consecutive days of de-identified event data collected from five sources within Los Alamos National Laboratory's corporate, internal computer network.
* [User-Computer Authentication Associations in Time](https://csr.lanl.gov/data/auth/) - This anonymized data set encompasses 9 continuous months and represents 708,304,516 successful authentication events from users to computers collected from the Los Alamos National Laboratory (LANL) enterprise network.
* [Canadian Institute for Cybersecurity datasets](https://www.unb.ca/cic/datasets/index.html) - Canadian Institute for Cybersecurity datasets are used around the world by universities, private industry and independent researchers.
* [KDD Cup 1999 Data](http://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html) - This database contains a standard set of data to be audited, which includes a wide variety of intrusions simulated in a military network environment.
* [2017-SUEE-data-set](https://github.com/vs-uulm/2017-SUEE-data-set) - The data sets contain traffic in and out of the web server of the Student Union for Electrical Engineering (Fachbereichsvertretung Elektrotechnik) at Ulm University. Internal hosts are hosts from within the university network, some of them are cable bound, others connect through one of two wifi services on campus (eduroam and welcome). The data was mixed with attack traffic.
* [CTU-13 Dataset](https://www.stratosphereips.org/datasets-ctu13/) -  A Labeled Dataset with Botnet, Normal and Background traffic.
* [PCAP files](https://www.netresec.com/index.ashx?page=PcapFiles) - Malware Traffic, Network Forensics, SCADA/ICS Network Captures, Packet Injection Attacks / Man-on-the-Side Attacks...
* [pcapt](https://www.pcapr.net) - Big repository of PCAP files.
* [Project Sonar](https://github.com/rapid7/sonar/wiki/UDP) - Project Sonar produces multiple UDP datasets every month. This data is gathered by sending protocol-specific UDP probes across the entire IPv4 address space. The types of probes sent each week continues to expand as the project matures.

### Malware
* [Malware Families Catalog](https://jordanricky1604-ship-it.github.io/malware-families-catalog/) - A massive catalog of 2,899 real-world malware families derived from the EMBER 2018 benchmark. Every family is categorized into 19 high-level threat types (Ransomware, InfoStealer, etc.) and mapped to MITRE ATT&CK tactics, with actionable incident response steps and dataset mirrors on Hugging Face, Kaggle, and Zenodo.
* [UNSW-NB15 data set](https://www.unsw.adfa.edu.au/unsw-canberra-cyber/cybersecurity/ADFA-NB15-Datasets/) - This data set has nine families of attacks, namely, Fuzzers, Analysis, Backdoors, DoS, Exploits, Generic, Reconnaissance, Shellcode and Worms. The Argus, Bro-IDS tools are utilised and twelve algorithms are developed to generate totally 49 features with the class label.
* [Malware Training Sets](https://marcoramilli.blogspot.com/2016/12/malware-training-sets-machine-learning.html) - Today (please refers to blog post date) the collected classified datasets is composed by the following samples: APT1 292 Samples, Crypto 2024 Samples, Locker 434 Samples, Zeus 2014 Samples
* [The Drebin Dataset](https://www.sec.cs.tu-bs.de/~danarp/drebin/) - The dataset contains 5,560 applications from 179 different malware families. The samples have been collected in the period of August 2010 to October 2012 and were made available to us by the MobileSandbox project.
* [Stratosphere IPS](https://www.stratosphereips.org/datasets-overview/) - Malware captures, Normal captures, mixed captures...
* [Microsoft Malware Classification Challenge](https://www.kaggle.com/c/malware-classification/data) - You are provided with a set of known malware files representing a mix of 9 different families. Each malware file has an Id, a 20 character hash value uniquely identifying the file, and a Class, an integer representing one of 9 family names.

### Software
* [Javascript Vulnerability dataset](http://www.inf.u-szeged.hu/~ferenc/papers/JSVulnerabilityDataSet/)  - Dataset constructed from the vulnerability information in public databases of the Node Security Project and the Snyk platform, and code fixing patches from GitHub.

### WebApps
* [Web Attack Payloads](https://github.com/foospidy/payloads) - A collection of web attack payloads.
* [Machine-Learning-driven-Web-Application-Firewall](https://github.com/faizann24/Fwaf-Machine-Learning-driven-Web-Application-Firewall) - Set of good and bad queries to a web application firewall.
* [Internet-Wide Scan Data Repository](https://scans.io/) - The Censys Projects publishes daily snapshots of what we know about each IPv4 host, Alexa Top Million website, and known X.509 certificate. These datasets contain structured, non-ephemeral JSON records that identify a host's configuration.
* [500K HTTP Headers](https://hackertarget.com/500k-http-headers/) - Recently we crawled the Top 500K sites (as ranked by Alexa). Following requests from readers we are making available the HTTP Headers for research purposes.
* [HTTP DATASET CSIC 2010](http://web.archive.org/web/20130924222653/http://iec.csic.es/dataset) - The HTTP dataset CSIC 2010 contains thousands of web requests automatically generated. It can be used for the testing of web attack protection systems. It was developed at the Information Security Institute of CSIC (Spanish Research National Council).
* [Common Crawl](http://commoncrawl.org/the-data/get-started/) - The Common Crawl corpus contains petabytes of data collected over the last 7 years. It contains raw web page data, extracted metadata and text extractions.
* [AZSecure-data](https://www.azsecure-data.org/get-data.html) - The AZSecure-data PORTAL currently provides access to Web forums, Internet phishing websites, Twitter data, and other data.

### URLs & Domain Names
* [Malicious URLs Dataset](http://www.sysnet.ucsd.edu/projects/url/) - The data set consists of about 2.4 million URLs (examples) and 3.2 million features.
* [Feodo Tracker](https://feodotracker.abuse.ch/) - List of Feodo botnet C&C servers
* [URLhaus](https://urlhaus.abuse.ch/api/) - URLhaus is a project from abuse.ch with the goal of sharing malicious URLs that are being used for malware distribution.
* [Alexa Top 1 Million](http://s3.amazonaws.com/alexa-static/top-1m.csv.zip) - CSV dataset with the most popular sites by Alexa.
* [OpenDNS Top Domains List](https://github.com/opendns/public-domain-lists) - The OpenDNS Top Domains List is the top 10,000 domain names our resolvers all over the globe are receiving queries for, sorted by popularity.
* [StopForumSpam](https://www.stopforumspam.com/downloads) - The data provided here represents what we believe will only ever ben used to abuse. IP Addresses, domains and usernames listed here will be returned in API results as "blacklisted".

### Host
* [The ADFA Intrusion Detection Datasets](https://www.unsw.adfa.edu.au/unsw-canberra-cyber/cybersecurity/ADFA-IDS-Datasets/) - This dataset provides a contemporary Linux dataset for evaluation by traditional HIDS. This dataset provides a contemporary Windows dataset for evaluation by HIDS.
* [Unified Host and Network Dataset](https://csr.lanl.gov/data/2017.html) - The Unified Host and Network Dataset is a subset of network and computer (host) events collected from the Los Alamos National Laboratory enterprise network over the course of approximately 90 days. The host event logs originated from most enterprise computers running the Microsoft Windows operating system on Los Alamos National Laboratory's (LANL) enterprise network. The network event data originated from many of the internal enterprise routers within the LANL enterprise network.
* [Public Security Log Sharing Site](http://log-sharing.dreamhosters.com/) - This site contains various free shareable log samples from various systems, security and network devices, applications, etc. The logs are collected from real systems, some contain evidence of compromise and other malicious activity. Wherever possible, the logs are NOT sanitized, anonymized or modified in any way (just as they came from the logging system).
* [Aktaion2 Data](https://github.com/jzadeh/aktaion2/tree/master/data) - The project is meant to be a learning/teaching tool on how to blend multiple security signals and behaviors into an expressive framework for intrusion detection.

### Email

### Fraud
* [Credit Card Fraud](https://www.kaggle.com/samkirkiles/credit-card-fraud/data) - The datasets contains transactions made by credit cards in September 2013 by european cardholders. This dataset presents transactions that occurred in two days, where we have 492 frauds out of 284,807 transactions. The dataset is highly unbalanced, the positive class (frauds) account for 0.172% of all transactions.

### Honeypots
* [DDS Dataset Collection](http://datadrivensecurity.info/blog/pages/dds-dataset-collection.html) - A tar/gzip CSV file from a collection of AWS honeypots. A zip CSV file of domains and a high level classification of dga or legit along with a subclass of either legit, cryptolocker, gox or newgoz.
* [Threat_Research](https://github.com/JonathanPhillips/Threat_Research) - Centralized repository to dump threat research data gathered from my network of honeypots.

### Binaries
* [The ember dataset](https://github.com/endgameinc/ember) - The ember dataset is a collection of 1.1 million sha256 hashes from PE files that were scanned sometime in 2017. This repository makes it easy to reproducibly train the benchmark model, extend the provided feature set, or classify new PE files with the benchmark model.

### Phishing
* [Phishing Websites Data Set](https://archive.ics.uci.edu/ml/datasets/phishing+websites#) - In this dataset, we shed light on the important features that have proved to be sound and effective in predicting phishing websites. In addition, we propose some new features.

### Passwords
* [Yahoo Password Frequency Corpus](https://figshare.com/articles/Yahoo_Password_Frequency_Corpus/2057937) - This dataset includes sanitized password frequency lists collected from Yahoo in May 2011.

### MISC
* [SecRepo](http://www.secrepo.com/) - Samples of Security Related Data.


### Generative AI & LLM Security
* [Jailbreak_LLMs](https://github.com/verazuo/jailbreak_llms) - A comprehensive dataset of thousands of prompt injection and jailbreak prompts used against Large Language Models in the wild.
* [LLM-Jailbreak-Classifier](https://huggingface.co/datasets/markush1/LLM-Jailbreak-Classifier-Dataset) - A Hugging Face dataset containing labelled safe and malicious prompts for training LLM guardrails.

### Modern Malware Benchmarks
* [SOREL-20M](https://github.com/sophos/SOREL-20M) - The Sophos-ReversingLabs 20 Million dataset. Released in late 2020, this is the modern benchmark for training PE malware detection models.
* [BODMAS](https://whyisyoung.github.io/BODMAS/) - Blue Hexagon Open Dataset for Malware Analysis. Features timestamped malware samples and behavioral vectors for temporal drift analysis.

### Cloud & Container Security
* [Mordor](https://github.com/OTRF/mordor) - The Mordor project provides pre-recorded, high-quality security events (JSON) generated by simulated adversarial techniques, heavily featuring cloud environments (AWS/Azure).
* [Flaws.cloud Logs](http://flaws.cloud/) - Log datasets from the famous AWS security challenges, providing real-world CloudTrail and S3 access logs of cloud compromise.

### Software Supply Chain
* [Backstabber's Knife Collection](https://github.com/das-group/bsk-dataset) - A curated dataset of open-source software supply chain attacks, containing malicious packages collected from NPM, PyPI, and RubyGems.
