#%%
from bs4 import BeautifulSoup
import json
import re

#%%
with open('./scratch/sdelovacka.html', 'r') as f:
    soup = BeautifulSoup(f)

#%%
oid = 0
txts = {}
cmnts = {}

for odst in soup.find_all('p', class_='c5'):
    oid += 1
    tx = odst.text
    for wr in [w for w in tx.split() if '[' in w]:
        tx = tx.replace(wr, '<span class="quote">' + wr.split('[')[0] +
        wr.split(']')[1] + '</span>')
    txts[oid] = tx

    for comment in odst.find_all('sup'):
        cid = comment.find('a').get('href').replace('#', '')
        for cpar in soup.find('a', id=cid).parent.parent.find_all('span', class_='c7'):
            if oid not in cmnts:
                cmnts[oid] = ''
            cmnts[oid] += cpar.text + '<br>'

#%%
with open('./js/data.js', 'w', encoding='utf-8') as f:
    f.write(
        'export const text = ' + json.dumps(txts, ensure_ascii=False) + '\n' +
        'export const comments = ' + json.dumps(cmnts, ensure_ascii=False)
    )
