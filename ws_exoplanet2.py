import pandas as pd
import numpy as np
import seaborn as sns

years=[2015,2016,2017,2018,2019]
str = 'https://www.basketball-reference.com/leagues/NBA_{}_per_game.html'
for year in years:
    url = str.format(year)
    print(url)

year='2019'
str = 'https://www.basketball-reference.com/leagues/NBA_{}_per_game.html'

url = str.format(year)
print(url)

df = pd.read_html(url, header=0)
print(df)

print(len(df))

df_2019 = df[0]
print(df[0])

df_age = df_2019[df_2019.Age == 'Age']
print(df_age)
print(len(df_age))

df2 = df_2019.drop(df_age.index)
print(df2)

#seaborn
sns.distplot(df2.PTS,  kde=False)