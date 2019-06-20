# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 17:08:13 2019

@author: Aditya Tanwar
"""


import pandas as pd
import numpy as np
#Read csv file
df = pd.read_csv("Telecom_churn.csv")
print(df)
df_sub1 = df['churn'][(df['voice mail plan']=='yes') & (df['international plan']=='yes') & (df['churn']==True)].count()
#both=df_sub1['voice mail plan'].count() and df_sub1['international plan'].count()
print("total no of churn customers",df_sub1)

df_sub2=df[(df['churn']==True)]
print("total Intl call charges for churn",df_sub2['total intl charge'])
df_sub3=df[(df['churn']==False)]
print("total Intl call charges for not churn",df_sub3['total intl charge'])

print(df_sub2['total night calls'].max())
df_sub4=df_sub2.groupby('state')[['state','total night calls']].max()
print(df_sub4.max())