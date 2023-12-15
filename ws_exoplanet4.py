import xml.etree.ElementTree as ET, urllib.request, gzip, io
url = "https://github.com/OpenExoplanetCatalogue/oec_gzip/raw/master/systems.xml.gz"
oec = ET.parse(gzip.GzipFile(fileobj=io.BytesIO(urllib.request.urlopen(url).read())))
print(oec) 
# Output mass and radius of all planets 
for planet in oec.findall(".//planet"):
    print([planet.findtext("mass"), planet.findtext("radius")])
 
# Find all circumbinary planets 
# for planet in oec.findall(".//binary/planet"):
#     print(planet.findtext("name"))
 
# Output distance to planetary system (in pc, if known) and number of planets in system
for system in oec.findall(".//system"):
# for planet in oec.findall(".//planet"):
    print("NAME : ",system.findtext("name"),
        "\t\t\tDISTANCE(pc) : ", system.findtext("distance"), 
        "\t\t\tnb PLANETE : ",len(system.findall(".//planet")),
        system.findtext("mass"), system.findtext("radius"),
        )

