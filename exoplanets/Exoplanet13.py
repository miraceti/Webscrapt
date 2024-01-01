import plotly.express as px
import pandas as pd
import numpy as np

#read csv to datafrtame
df7 = pd.read_csv('exoplanet_2023.csv', sep=',')
#df7=df7.dropna(axis=1)
print(df7)
df7['pl_bmasse']=df7['pl_bmasse'].replace(np.nan,0)
df_method = df7.groupby(['discoverymethod'])['pl_name'].count()
print(df_method)
data = [['Astrometry',df_method['Astrometry']],['Disk Kinematics',df_method['Disk Kinematics']],
        ['Eclipse Timing Variations',df_method['Eclipse Timing Variations']],['Imaging',df_method['Imaging']],
        ['Microlensing',df_method['Microlensing']],['Orbital Brightness Modulation',df_method['Orbital Brightness Modulation']],
        ['Pulsar Timing',df_method['Pulsar Timing']],['Pulsation Timing Variations',df_method['Pulsation Timing Variations']],
        ['Radial Velocity',df_method['Radial Velocity']],['Transit',df_method['Transit']],
        ['Transit Timing Variations',df_method['Transit Timing Variations']]]

df_method1 = pd.DataFrame(data, columns=['method_name','method_count'])
print(df_method1)

fig = px.pie(df_method1, values='method_count', names='method_name')
fig.show()