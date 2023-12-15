# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

print("hello")
import bs4
import requests
from bs4 import BeautifulSoup

#"prix
def parseprice():
    r = requests.get('https://finance.yahoo.com/quote/FB?p=FB')
    soup = bs4.BeautifulSoup(r.text,"xml")
    price=soup.find('span',class_='Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)')
    return price

#while True:


