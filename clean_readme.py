import re

dead_urls = [
    'research.aalto.fi/en/datasets/iot-devices-captures',
    'www.westpoint.edu/crc/SitePages/DataSets.aspx',
    'www.uvic.ca/engineering/ece/isot/datasets/index.php',
    'www.secrepo.com/self.logs/',
    'data.webarchive.org.uk/opendata/ukwa.ds.1/classification/',
    'www.malwaredomainlist.com/forums/index.php?topic=3270.0',
    'zeustracker.abuse.ch',
    'ransomwaretracker.abuse.ch/blocklist',
    'majestic.com/reports/majestic-million',
    'plg.uwaterloo.ca/~gvcormac/treccorpus07/about.html',
    'techhelplist.com/spam-list',
    'www.rrshare.org',
    'bigdata.ise.bgu.ac.il/sherlock',
    'decal.github.io/werdlists',
    'cybercrime-tracker.net'
]

with open('README.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    is_dead = False
    for dead_url in dead_urls:
        if dead_url in line:
            is_dead = True
            print(f'Removing line: {line.strip()}')
            break
    if not is_dead:
        new_lines.append(line)

with open('README.md', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print('README.md cleaned.')
