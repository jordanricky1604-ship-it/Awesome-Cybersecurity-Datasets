import urllib.request
import json
try:
    url = 'https://jordanricky1604-ship-it.github.io/Awesome-Cybersecurity-Datasets/datasets.json'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    r = urllib.request.urlopen(req)
    data = json.loads(r.read().decode('utf-8'))
    print(f'Live datasets.json length: {len(data)}')
    print('Sample new datasets found online:')
    for d in data[-5:]:
        print(f"- {d['name']} ({d['category']})")
except Exception as e:
    print(f'Error: {e}')
