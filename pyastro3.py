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

print(epl.dataAge())

print(epl.needsUpdate())

e = epl.getAllData()

df = pd.DataFrame(e)
print(df)