# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 09:28:00 2018

@author: DanielFryy
"""

import pandas as pd
import os

df = pd.read_pickle('C://Users//danie//Dropbox//EPN//2018-B//Python//freire-gonzalez-daniel-enrique//03_Spyder//data//artwork_data_frame.pickle')

df.loc[1035, 'artist']

# df.loc[0, 0] Error

df.iloc[0, 0]
df.iloc[0, :]
df.iloc[:2, :2]

df['height']
df['width']

# df['height'] * df['width']

df_width = df['width']
dfsort_values = df['width'].sort_values()
dfsort_values_head = df['width'].sort_values().head()
dfsort_values_tail = df['width'].sort_values().tail()

# pd.to_numeric(df['width'])
width_numeric = pd.to_numeric(df['width'], errors='coerce')
height_numeric = pd.to_numeric(df['height'], errors='coerce')

df.loc[:, 'width'] = width_numeric
df.iloc[:, 6] = height_numeric

area = df['height'] * df['width']
df = df.assign(area = area)

df_area = df['area'].sort_values(ascending=False).head(1)
id_max_area = df['area'].idxmax()
id_min_area = df['area'].idxmin()

nuevo = ['9999999', 'Daniel Freire', 'Pintura', 'Marco Lienzo Pintura', 2000, 2005, 200, 500, 'mm', 100000]
serie_nuevo = pd.Series(nuevo, index = ['index'] + list(df))
df2 = df.append(serie_nuevo, ignore_index=True)
