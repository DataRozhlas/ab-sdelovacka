#%%
from bs4 import BeautifulSoup
import json

#%%
with open('./scratch/sdelovacka.html', 'r') as f:
    soup = BeautifulSoup(f)

#%%
oid = 0
txts = {}
cmnts = {}

for odst in soup.find_all('p', class_='c5'):
    oid += 1
    txts[oid] = odst.text

    for comment in odst.find_all('sup'):
        cid = comment.find('a').get('href').replace('#', '')
        for cpar in soup.find('a', id=cid).parent.parent.find_all('span', class_='c7'):
            if oid not in cmnts:
                cmnts[oid] = ''
            cmnts[oid] += cpar.text + '<br>'

#%%
cpar.parent.parent

#%%
with open('./js/data.js', 'w', encoding='utf-8') as f:
    f.write(
        'export const text = ' + json.dumps(txts, ensure_ascii=False) + '\n' +
        'export const comments = ' + json.dumps(cmnts, ensure_ascii=False)

    )

#%%
cid

#%%
