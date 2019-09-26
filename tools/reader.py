#%%
from bs4 import BeautifulSoup
import json
import re
import markdown

#%%
with open('./scratch/obvinnAABBdokument25stran.docx.html', 'r') as f:
    soup = BeautifulSoup(f)

#%%
oid = 0
txts = {}
cmnts = {}

for odst in soup.find_all('p', class_=['c12', 'c6']):
    oid += 1
    tx = markdown.markdown(odst.text).replace('<p>', '').replace('</p>', '')
    for wr in [w for w in tx.split() if '[' in w]:
        tx = tx.replace(wr, '<span class="quote">' + wr.split('[')[0] +
        wr.split(']')[1] + '</span>')
    txts[oid] = tx

    for comment in odst.find_all('sup'):
        cid = comment.find('a').get('href').replace('#', '')
        for cpar in soup.find('a', id=cid).parent.parent.find_all('span', class_='c11'):
            ctx = cpar.text
            ctx = ctx.replace('] (', '](').replace(']\n(', '](')
            if oid not in cmnts:
                cmnts[oid] = ''
            cmnts[oid] += markdown.markdown(cpar.text).replace('<p>', '').replace('</p>', '') + '<br><br>'

#%%
with open('./js/text.js', 'w', encoding='utf-8') as f:
    f.write(
        'export const text = ' + json.dumps(txts, ensure_ascii=False, indent=4, separators=(',', ': '))
    )

with open('./js/comments.js', 'w', encoding='utf-8') as f:
    f.write(
        'export const comments = ' + json.dumps(cmnts, ensure_ascii=False, indent=4, separators=(',', ': '))
    )

#%%
print(len(cmnts), len(txts))

#%%