import json
import urllib.request
import urllib.error
import ssl
from concurrent.futures import ThreadPoolExecutor

filepath = r"c:\Users\Nishant Tandon\.gemini\antigravity\scratch\Awesome-Cybersecurity-Datasets\datasets.json"

with open(filepath, 'r', encoding='utf-8') as f:
    datasets = json.load(f)

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def check_url(dataset):
    url = dataset['url']
    req = urllib.request.Request(
        url, 
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    )
    try:
        response = urllib.request.urlopen(req, context=ctx, timeout=10)
        if response.getcode() < 400:
            dataset['status'] = 'active'
        else:
            dataset['status'] = 'dead'
    except urllib.error.HTTPError as e:
        if e.code in [401, 403]: # Might just be blocking bots
            dataset['status'] = 'active'
        else:
            dataset['status'] = 'dead'
    except Exception as e:
        dataset['status'] = 'dead'
        
    return dataset

print("Validating 53 links...")
with ThreadPoolExecutor(max_workers=10) as executor:
    results = list(executor.map(check_url, datasets))

active_count = sum(1 for d in results if d['status'] == 'active')
dead_count = sum(1 for d in results if d['status'] == 'dead')

print(f"Validation complete: {active_count} Active, {dead_count} Dead.")

# Purge dead links
valid_datasets = [d for d in results if d['status'] == 'active']

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(valid_datasets, f, indent=4)

print("Saved validated datasets.json")
