from bs4 import BeautifulSoup
import requests
import json
import pandas as pd
import json

url=requests.get('http://digidb.io/digimon-list/')
soup=BeautifulSoup(url.content,'html.parser')
url = soup.find('table', id='digiList')

listurl=[]
for i in soup.find_all('th'):
    listurl.append(i.string)

listdigimon=[]
url=url.find_all('tr')

for item in url[1:]:
    no=item.td.string
    name=item.a.string
    img=item.img['src']
    stage=item.center.string
    typedigi=item.td.find_next_sibling().find_next_sibling().find_next_sibling()
    attribute=item.td.find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling()
    memory=attribute.find_next_sibling()
    equip=memory.find_next_sibling()
    hp=equip.find_next_sibling()
    sp=hp.find_next_sibling()
    atk=sp.find_next_sibling()
    defense=atk.find_next_sibling()
    intelligence=defense.find_next_sibling()
    speed=intelligence.find_next_sibling()
    x={
        'no':int(no),
        'digimon':name,
        'image':img,
        'stage':stage,
        'type':typedigi.string,
        'attribute':attribute.string,
        'memory':memory.string,
        'equip slots':equip.string,
        'hp':hp.string,
        'sp':sp.string,
        'atk':atk.string,
        'def':defense.string,
        'int':intelligence.string,
        'spd': speed.string}
    listdigimon.append(x)

with open('digimon.json','w') as x:
    json.dump(listdigimon, x)
