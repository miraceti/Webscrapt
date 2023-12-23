# from __future__ import print_function, division
from astroquery.ipac.nexsci.nasa_exoplanet_archive import NasaExoplanetArchive

# from PyAstronomy import pyasl
# import matplotlib.pylab as plt
import pandas as pd

#recupearation all planets
# exoplanets_table = NasaExoplanetArchive.get_comfirmed_planets_table()

#afficher les données des exoplanetes
print('\nNEA : TAP_TABLES :\n',NasaExoplanetArchive.TAP_TABLES)

# print(NasaExoplanetArchive.query_object("K2-18 b"))

t0 =NasaExoplanetArchive.query_criteria(table="pscomppars", 
                                        select="pl_name"
                                        #,where="pl_name like '%Kepler-10 %'"
                                       )
df0= t0.to_pandas()
print('\nNombre de lignes : ',len(df0),'\n',df0)



# t3 =NasaExoplanetArchive.query_criteria(table="pscomppars", select="top 10 *")
# df3 = t3.to_pandas()
# colons = df3.columns.tolist()
# colonst = colons.sort()
# print('\nNombre de colonnes : ',len(colons),'\n', colons,'\nNombre de lignes : \n',len(df3),'\n',df3)

t4 =NasaExoplanetArchive.query_criteria(table="pscomppars", 
                                        select="pl_name,discoverymethod,disc_year,pl_bmasse"
                                        ,where="pl_name like '%Kepler-10 %'"
                                       )
df4= t4.to_pandas()
print('\nNombre de lignes : ',len(df4),'\n',df4)


t5 =NasaExoplanetArchive.query_criteria(table="pscomppars", 
                                        select=" distinct discoverymethod"
                                        #,where="discoverymethod like '%imagi%'"
                                       )
df5= t5.to_pandas()
print('\nNombre de lignes : ',len(df5),'\n',df5)

t6 =NasaExoplanetArchive.query_criteria(table="pscomppars", 
                                        select=" distinct pl_name,discoverymethod,disc_year,pl_bmasse"
                                        ,where="discoverymethod like '%Imag%'"
                                        ,order="disc_year desc"
                                       )
df6= t6.to_pandas()
print('\nNombre de lignes : ',len(df6),'\n',df6)