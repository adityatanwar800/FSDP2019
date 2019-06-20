# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 15:48:48 2019

@author: Aditya Tanwar
"""

import pandas as pd
#Read csv file
df = pd.read_csv("training_titanic.csv")
#print (df)

#to find total no. of survived count where survived=1
df['Survived'].count()
df_sub = df[df['Survived'] == 1]
#print(df_sub)
print("total no. of Survived ")
print(df_sub['Survived'].count())

#to find total no. of died, total-survived=died
print("total no. of died ")
died=df['Survived'].count()-df_sub['Survived'].count()
print(died)


#no of female alive
df_sub1 = df[(df['Sex']=='female') & (df['Survived']==1)]
print("total no. of female Survived",df_sub1['Sex'].count())
#no female died
df_sub2= df[(df['Sex']=='female')]

died=df_sub2['Sex'].count()-df_sub1['Sex'].count()
print("total no. of female not Survived",died)

#no of male alive
df_sub1 = df[(df['Sex']=='male') & (df['Survived']==1)]
print("total no. of male Survived",df_sub1['Sex'].count())
#no male died
df_sub2= df[(df['Sex']=='male')]

died=df_sub2['Sex'].count()-df_sub1['Sex'].count()
print("total no. of male not Survived",died)


#survial rate by normalize =True
print("survial rate")
df['Survived'].value_counts(normalize = True)



df["child"] = df["Age"].map(lambda x: 0 if x >=18 else 1 )
print(df)

