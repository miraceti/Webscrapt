# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 18:38:08 2020

@author: eric
"""

from __future__ import print_function, division
from PyAstronomy import pyasl
import pandas as pd

# Instantiate the access class
epl = pyasl.ExoplanetsOrg()

# Show the available columns
epl.availableColumns()

# Get information in Kepler-5 b
d = epl.selectByPlanetName("kepler-5 b")

# Print whatever information has been received
print()
print("Information on Kepler-5 b")
print()
for k, v in list(d.items()):
  print("%12s  %12s" % (k,str(v)))

# Get information in Kepler-5 b
e = epl.getAllData()

# Print whatever information has been received
print()
print("Information on all")
print()
print(len(e))
print(type(e))

df = pd.DataFrame(e)
print(df)