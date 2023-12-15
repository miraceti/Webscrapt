import requests
from bs4 import BeautifulSoup
import pandas as pd

print(BeautifulSoup(requests.get('https://nssdc.gsfc.nasa.gov/planetary/factsheet/index.html').content, 'lxml'))

soup =BeautifulSoup(requests.get('https://nssdc.gsfc.nasa.gov/planetary/factsheet/index.html').content, 'lxml').find('table').findAll('tr')
print(soup)

soup1 = [[j.text.replace(u'\xa0', '').replace('*','').replace(',','') for j in i.findAll('td')] for i in BeautifulSoup(requests.get('https://nssdc.gsfc.nasa.gov/planetary/factsheet/index.html').content, 'lxml').find('table').findAll('tr')]
print (soup1)

table = soup1

tablehead = [i.pop(0) for i in table]
print(tablehead)

print(table)

print(dict(zip(tablehead, table)))

dataframe = pd.DataFrame(dict(zip(tablehead, table)))
print(dataframe)
#dataframe.to_csv('D:/SITE/FREE/jeux/python/webscrap/planetdata.csv', index=False )
dataframe.to_csv('planetdata.csv', index=False )