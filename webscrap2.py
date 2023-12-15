# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 20:52:16 2019

@author: eric
"""

import requests
from bs4 import BeautifulSoup

url='https://www.ebay.com/b/Samsung-Cell-Phones-and-Smartphones/9355/bn_352130'
    
#"def get_page(url):
response = requests.get(url)
#print(response.content)    
if not response.ok:
    print('server : ', response.status_code)
else:
    soup = BeautifulSoup(response.text,'lxml')
#    return soup

#def get_detail_data(soup):
h1 = soup.find_all('div', class_='b-info')
#print(h1)
print('H2')
h2 = h1[0].text
print(h2)
h3 = soup.find_all('div', class_='b-info__title')[0].text
print(h3)

    

#def main():
   
#    p =   get_page(url)  
#    get_detail_data(p)
    
#if __name__ == '__main__':
#    main()