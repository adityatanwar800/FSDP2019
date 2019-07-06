# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 10:57:51 2019

@author: Aditya Tanwar
"""

import pandas as pd
from apyori import apriori
import matplotlib.pyplot as plt

# Data Preprocessing
dataset = pd.read_csv('BreadBasket_DMS.csv')
dataset.isnull().any(axis=0)
#sorted dataframe by Transaction
dataset1= dataset.sort_values(by='Transaction',ascending=False)
#pie chart of items top 15
x=list(dataset1['Transaction'].head(15))
label=list(dataset1['Item'].head(15))
plt.pie(x,labels=label)
plt.show()


#nested list
z = [[i] for i in dataset['Transaction'].unique().tolist()]
Y = [i for i in dataset['Item'].tolist()]

for key, value in enumerate(z):
    z[key].append(Y[key])