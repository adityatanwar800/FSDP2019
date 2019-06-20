# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 16:51:09 2019

@author: Aditya Tanwar
"""

import pandas as pd
import numpy as np
#Read csv file
df = pd.read_csv("Automobile.csv")
print(df)
df[df['price'].isnull()]
df_copy = df.copy().dropna(how='any')
print(df_copy)
df1=df["price"]
x = np.array(df1 ) 
print (type(x))
df['price'].describe()