from astroquery import open_exoplanet_catalogue as oec
from astroquery.open_exoplanet_catalogue import findvalue

# getting the catalogue from the default remote source
cata = oec.get_catalogue()
print(cata)
#Prints all planets and their masses.

for planet in oec.findall(".//planet"):
    print(findvalue(planet, 'name'), findvalue(planet, 'mass'))

# kepler68b = cata.find(".//planet[name='Kepler-68 b']")
# print(findvalue( kepler68b, 'mass'))

# for planet in cata.find(".//planet"):
#     print(findvalue(planet, 'name'), findvalue(planet, 'mass'))