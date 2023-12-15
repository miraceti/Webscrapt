# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 22:55:13 2019

@author: eric
"""

import requests
from bs4 import BeautifulSoup
import csv

#r = requests.get('https://www.usclimatedata.com/climate/united-states/us')
r = requests.get('https://exoplanets.nasa.gov/exoplanet-catalog/')
#print(len(r.text))

soup = BeautifulSoup(r.text,'html5lib')
hi= soup.select('title')
print(hi)
print(hi[0].get_text())