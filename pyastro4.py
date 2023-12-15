from __future__ import print_function, division
from PyAstronomy import pyasl
import matplotlib.pylab as plt
import pandas as pd

eu = pyasl.ExoplanetEU()

# See what information is available
cols = eu.availableColumns()
print(cols)

print()
# Get all data and plot planet Mass vs.
# semi-major axis in log-log plot
dat = eu.getAllData()
print(dat)

df = pd.DataFrame(dat)
print(df)

plt.xlabel("Planet Mass [RJ]")
plt.ylabel("Semi-major axis [AU]")
plt.loglog(dat.plMass, dat.sma, 'b.')
plt.show()