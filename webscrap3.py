# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 21:45:13 2019

@author: eric
"""
import requests
from bs4 import BeautifulSoup
url='http://example.webscraping.com/places/default/view/Australia-14'
#url = 'https://www.ebay.com/b/Samsung-Cell-Phones-and-Smartphones/9355/bn_352130'

r = requests.get(url)

soup = BeautifulSoup(r.content,'html5lib')
#soup = BeautifulSoup(r.content,'xml')

#print(soup.prettify())

population = soup.find('tr',attrs={'id':'places_population__row'})
#print(str(population))

population_data=population.find('td',attrs={'class':'w2p_fw'})
#print(str(population_data.text))

table = soup.find('table')
#print(table)
trs =  table.findAll('tr')

for tr in trs:
#    print(tr)
    keys = tr.find('td',attrs={'class':'w2p_fl'})
    values = tr.find('td',attrs={'class':'w2p_fw'})
    print(str(keys.text)+" : "+str(values.text))