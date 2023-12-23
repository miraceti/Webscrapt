from __future__ import print_function, division
from astroquery.ipac.nexsci.nasa_exoplanet_archive import NasaExoplanetArchive

from PyAstronomy import pyasl
import matplotlib.pylab as plt
import pandas as pd

#recupearation all planets
# exoplanets_table = NasaExoplanetArchive.get_comfirmed_planets_table()

#afficher les données des exoplanetes
print(NasaExoplanetArchive.TAP_TABLES)

print()
# # Get all data and plot ra vs. dec
# dat = nexa.getAllData()
# df = pd.DataFrame(dat)
# print(df)

# plt.plot(dat.ra, dat.dec, 'b.')
# plt.show()

print(NasaExoplanetArchive.query_object("K2-18 b"))


nexa = pyasl.NasaExoplanetArchive()
dat1 = nexa.getAllData()
df1 = pd.DataFrame(dat1)
print('DF1 : ',df1)


t2 =NasaExoplanetArchive.query_criteria(table="pscomppars", select="count(*)",
                                    where="disc_facility like '%TESS%'") 
print(t2)

t3 =NasaExoplanetArchive.query_criteria(table="pscomppars", select="*",
                                    where="disc_facility like '%TESS%'") 
print('T3 : ',t3)
print(type(t3))
df3 = t3.to_pandas()
print(type(df3))
print('DF3 : ',df3.columns)
print(list(df3.columns.values))

# Get the list of all column names from headers
column_headers = df3.columns.values.tolist()
print("\nThe Column Header 1 :\n", column_headers)

# Using list(df) to get the column headers as a list
column_headers = list(df3.columns)
print("\nThe Column Header 2 :\n", column_headers)

# Using list(df) to get the list of all Column Names
column_headers = list(df3)
print("\nThe Column Header 3 :\n", column_headers)

# Dataframe show all columns sorted list
col_headers=sorted(df3)
print("\nThe Column Header 4 :\n", col_headers)

# Get all Column Header Labels as List
lene = 0
for column_headers in df3.columns: 
    lene +=1
print("\n Nombre de colonnes 5 :\n",lene)

# Get column header using keys() method  
column_headers = df3.keys().values.tolist()
print("\nThe Column Header 6 :\n", column_headers)

# Get all numeric columns
numeric_columns = df3._get_numeric_data().columns.values.tolist()
print("\nThe Column Header 7 :\n", numeric_columns)

