# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 21:48:59 2019

@author: eric
"""

import requests
from bs4 import BeautifulSoup
import csv

r = requests.get('https://www.usclimatedata.com/climate/united-states/us')
#r = requests.get('https://exoplanets.nasa.gov/exoplanet-catalog/')
print(len(r.text))

soup = BeautifulSoup(r.text,'html5lib')
print(soup.title)
print(soup.title.string)
print(soup.p)
print(soup.p.text)
print(soup.a)
print(soup.a['title'])
print()
print(soup.p.parent)
print(soup.p.parent.prettify())

for link in soup.find_all('a'):
    print(link.get('href'))
    
print()

base_url = 'https://www.usclimatedata.com'
#base_url = 'https://exoplanets.nasa.gov/exoplanet-catalog'  
state_links =[]
for link in soup.find_all('a'):
    url = link.get('href')
    if url and '/climate/' in url and '/climate/united-states/us' not in url:
        state_links.append(url)
print(len(state_links))

r=requests.get(base_url + state_links[5])
soup = BeautifulSoup(r.text,'html5lib')
print(soup.title.string)

print()
rows = soup.find_all('tr')
print(len(rows))

rows = [row for row in rows if 'Average high' in str(row)]
print(len(rows))

high_temps =[]
for row in rows:
    tds = row.find_all('td')
    for i in range(1,7):
        high_temps.append(tds[i].text)
print(high_temps)


print()

state = soup.title.string.split()[1]
print(state)

s = soup.title.string
state = s[s.find(' '):s.find('-')].strip()
print(state)


data = {}
data[state]=high_temps
print(data)

#on boucle pour tous les etats
print('****************************************')
data = {}
for state_link in state_links:
    base_url + state_link
    r=requests.get(base_url + state_link)
    soup = BeautifulSoup(r.text,'html5lib')
    rows = soup.find_all('tr')
    rows = [row for row in rows if 'Average high' in str(row)]
    high_temps =[]
    for row in rows:
        tds = row.find_all('td')
        for i in range(1,7):
            high_temps.append(tds[i].text)
        
    s = soup.title.string
    state = s[s.find(' '):s.find('-')].strip()    
    data[state]=high_temps    
    print(data)    
        
#csv file
with open('high_temps.csv','w') as f:
    w = csv.writer(f)
    w.writerows(data.items())
        
        
        
        
    
    
    
    
    
    
    
    



