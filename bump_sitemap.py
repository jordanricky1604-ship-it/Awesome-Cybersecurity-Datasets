import re
from datetime import datetime
import os

today = datetime.now().strftime("%Y-%m-%d")

if os.path.exists('sitemap.xml'):
    with open('sitemap.xml', 'r', encoding='utf-8') as f:
        content = f.read()
    content = re.sub(r'<lastmod>[0-9]{4}-[0-9]{2}-[0-9]{2}</lastmod>', f'<lastmod>{today}</lastmod>', content)
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated sitemap.xml to", today)
