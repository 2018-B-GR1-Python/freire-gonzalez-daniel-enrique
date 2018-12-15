# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 09:19:59 2018

@author: DanielFryy
"""

import pandas as pd
import os
import numpy as np
import sqlite3

df = pd.read_pickle('C://Users//danie//Dropbox//EPN//2018-B//Python//freire-gonzalez-daniel-enrique//03_Spyder//data//artwork_data_frame.pickle')
df_section = df.iloc[49980:50019,:].copy()

# to sql
with sqlite3.connect('C://Users//danie//Dropbox//EPN//2018-B//Python//freire-gonzalez-daniel-enrique//03_Spyder//my_database.db') as connection:
    df_section.to_sql('Tate', connection)

# to JSON
df_section.to_json('C://Users//danie//Dropbox//EPN//2018-B//Python//freire-gonzalez-daniel-enrique//03_Spyder//test.json')
df_section.to_json('C://Users//danie//Dropbox//EPN//2018-B//Python//freire-gonzalez-daniel-enrique//03_Spyder//test2.json', orient='table')

# to Excel
df_section.to_excel('C://Users//danie//Dropbox//EPN//2018-B//Python//freire-gonzalez-daniel-enrique//03_Spyder//basic.xlsx')
df_section.to_excel('C://Users//danie//Dropbox//EPN//2018-B//Python//freire-gonzalez-daniel-enrique//03_Spyder//basic_witout_index.xlsx', index = False)
df_section.to_excel('C://Users//danie//Dropbox//EPN//2018-B//Python//freire-gonzalez-daniel-enrique//03_Spyder//just_some_columns.xlsx', columns = ['artist', 'title', 'year'])

# Multiple sheets
writer = pd.ExcelWriter('C://Users//danie//Dropbox//EPN//2018-B//Python//freire-gonzalez-daniel-enrique//03_Spyder//multiple_sheets.xlsx', engine = 'xlsxwriter')
df_section.to_excel(
        writer,
        sheet_name = 'Preview',
        index = False)

# Conditional formating
counted_artist = df['artist'].value_counts()

counted_artist.head()

writer = pd.ExcelWriter('C://Users//danie//Dropbox//EPN//2018-B//Python//freire-gonzalez-daniel-enrique//03_Spyder//colours.xlsx', engine = 'xlsxwriter')

counted_artist.to_excel(
        writer,
        sheet_name = 'Artist Count')

sheet = writer.sheets['Artist Count']

cells_range = 'B2:B{}'.format(len(counted_artist.index))

sheet.conditional_format(cells_range, {
        'type':'2_color_scale',
        'min_value':'10',
        'min_type':'percentile',
        'max_value':'99',
        'max_type':'percentile',
        })