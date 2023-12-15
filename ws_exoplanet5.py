from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
# url = 'https://en.wikipedia.org/wiki/List_of_exoplanets_discovered_in_2023'

page = requests.get(url)

soup = BeautifulSoup(page.text,features="html")

# print(soup)

# <table class="wikitable plainrowheaders sortable jquery-tablesorter" 
table_1t = soup.find('table')
# print(table_1t)

table_at = soup.find_all('table')[1]
print(table_at)


table_001 = soup.find('table', classe='wikitable plainrowheaders sortable jquery-tablesorter')
# print(table_001)

#titre
world_titres = table_at.find_all('th')
print(world_titres)

world_table_titres = [titre.text.strip() for titre in world_titres ]
print(world_table_titres)

df = pd.DataFrame(columns=world_table_titres)
print(df)

column_data = table_at.find_all('tr')

for row in column_data:
    print(row.find_all('td'))

#dans une liste
for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data ]
    print(individual_row_data)

    length = len(df)
    df.loc[length] = individual_row_data

print(df)

df.to_csv(r'D:\SITE\FREE\jeux\python\webscrap\companies.csv')

df.to_csv(r'D:\SITE\FREE\jeux\python\webscrap\companies_no_index.csv', index=False)