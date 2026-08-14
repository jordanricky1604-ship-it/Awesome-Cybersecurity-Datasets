import urllib.request
import re
import socket

socket.setdefaulttimeout(5)

with open('README.md', 'r', encoding='utf-8') as f:
    content = f.read()

urls = re.findall(r'\[.*?\]\((http.*?)\)', content)

alive = []
errors = []

for url in urls:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        res = urllib.request.urlopen(req)
        if res.getcode() == 200:
            alive.append(url)
        else:
            errors.append((url, res.getcode()))
    except Exception as e:
        errors.append((url, str(e)))

print(f'Total URLs: {len(urls)}')
print(f'Alive: {len(alive)}')
print(f'Errors: {len(errors)}')

for url, err in errors:
    print(f'ERROR: {url} - {err}')
