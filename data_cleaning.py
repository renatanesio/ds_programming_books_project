# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 2020

@author: renatanesio
"""

import pandas as pd

df = pd.read_csv('prog_book.csv')

df['Reviews'] = df['Reviews'].str.replace(',','')
df['Reviews'] = df['Reviews'].astype(int) 

cleanup_types = {"Type": {"Hardcover": 1, "Boxed Set - Hardcover": 2, 
                          "Paperback": 3, "Kindle Edition": 4,
                          "ebook": 5, "Unknown Binding": 6}}

df.replace(cleanup_types, inplace=True)
 

df_out = df.drop(['Book_title', 'Description'], axis=1)

df_out.to_csv("book_data_cleaned.csv", index = False)
