# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 07:27:26 2018

@author: DanielFryy
"""

import pandas as pd
import os
import numpy as np
import math

df = pd.read_pickle('C://Users//danie//Dropbox//EPN//2018-B//Python//freire-gonzalez-daniel-enrique//03_Spyder//data//artwork_data_frame.pickle')

df_section = df.iloc[49980:50019,:].copy()

# group by

grouped_df = df_section.groupby('artist')

for name, group_fd in grouped_df:
    print(f'Artista: {name}')
    print(group_fd)
    min_year = group_fd['acquisitionYear'].min()
    print(f'{min_year}')
    print('{}:{}'.format(name, min_year))
    
def fill_empty_values(series):
    # print(series)
    counted_values = series.value_counts()
    if counted_values.empty:
        return series
    """
    # print(counted_values)
    sums = 0
    nans = 0
    for value in series:
        if type(value) == str:
            sums += int(value)
        if type(value) == float:
            nans = nans + 1
    div = series.size - nans
    most_used_value = sums / div
    """
    # print(counted_values)
    # print(counted_values.index[0])
    new_value = series.fillna(counted_values.index[0])
    return new_value

def transform_df_by_artist(df):
    grouped_by_artist = df.groupby('artist')
    df_array_by_group = []
    # print(grouped_by_artist)
    for name, group in grouped_by_artist:
        filled_df = group.copy()
        # print(group['medium'])
        filled_df.loc[:,'medium'] = fill_empty_values(group['medium'])
        # print(filled_df)
        df_array_by_group.append(filled_df)
    new_filled_df = pd.concat(df_array_by_group)
    return new_filled_df

tranformed_section = transform_df_by_artist(df_section)

df_grouped_by_title = df.groupby('title')
counted_titles = df_grouped_by_title.size().sort_values(ascending = False)
print(counted_titles)
condition = lambda x : len(x.index) > 1
dup_titles_df = df_grouped_by_title.filter(condition)
print(dup_titles_df)
dup_titles_df.sort_values('title', inplace = True)
print(dup_titles_df.sort_values('title', inplace = True))