# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 09:56:51 2018

@author: DanielFryy
"""

import pandas as pd
import os

CSV_PATH = "C://Users//danie//Dropbox//EPN//2018-B//Python//freire-gonzalez-daniel-enrique//03_Spyder//data//artwork_data.csv"

# 1) Archivos de texto -> CSV, JSON, HTML
# 2) Binary Files
# 3) Relational Databases

data_frame_artwork = pd.read_csv(
        CSV_PATH,
        nrows = 5,
        index_col = 'id',
        usecols = ['id', 'artist'])

columnas_a_utilizar = ['id', 'artist', 'title','medium', 'year',
                       'acquisitionYear', 'height', 'width', 'units']

data_frame_artwork_completo = pd.read_csv(
        CSV_PATH,
        index_col = 'id',
        usecols = columnas_a_utilizar)

# --> Serializacion del DataFrame
# --> Deserializacion del DataFrame

PATH_GUARDADO = "C://Users//danie//Dropbox//EPN//2018-B//Python//freire-gonzalez-daniel-enrique//03_Spyder//data//artwork_data_frame.pickle"
data_frame_artwork_completo.to_pickle(PATH_GUARDADO)

df_completo_pickle = pd.read_pickle(PATH_GUARDADO)
