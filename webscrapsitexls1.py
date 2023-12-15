# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 10:44:11 2020

@author: eric
"""

# beautiful soup libraries
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re 
import win32com.client
import numpy as np

# Get our Excel App
ExcelApp = win32com.client.gencache.EnsureDispatch('Excel.Application')

# Get our Worksheet
WrkSht = ExcelApp.ActiveSheet

# Define Range of URl
Url_List = WrkSht.Range("A1:C1").Value

# Define a section initalizer, 
# this will make sure we dump the urls in the proper column.
section_init = 1

# Loop through each url in the url_list
for url in Url_List[0]:
    
    # Request the URL, and initialize the list that will store the URLs
    req = Request(url)
    html_page = urlopen(req)
    print(req)
    column_list =[]
    
    # Get the HTML content
    soup = BeautifulSoup(html_page, 'html.parser')
    
    # Loop through each of HREF links and store them in the list.
    for link in soup.findAll('a'):
        row_list = []
        row_list.append(link.get('href'))
        column_list.append(row_list)

    # Dump the urls in the proper sections.
    StrCell = WrkSht.Cells(2, section_init)
    EndCell = WrkSht.Cells(2 + len(column_list), section_init)    
    ExcelApp.Range(StrCell, EndCell).Value = column_list
    
    # Make sure to initalize the next section.
    section_init += 1