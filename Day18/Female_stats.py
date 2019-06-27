# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 16:29:13 2019

@author: Aditya Tanwar
"""

import pandas as pd
import matplotlib.pyplot as plt

# Importing the dataset
dataset = pd.read_csv('Female_Stats.csv')
#temp = dataset.values
features = dataset.iloc[:,1:].values
labels = dataset.iloc[:,0 ].values

import statsmodels.api as sm
#adds a constant column to input data set
features = sm.add_constant(features)

features_opt = features[:, [0, 1, 2]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()

# Visualising the data
plt.scatter(features[:,1], labels)
plt.scatter(features[:,2], labels)

# When Father's height is constant 
print("1 inch change in mom's height -> {} inch chnage in son's height"\
      .format(round(regressor_OLS.params[2],2)))
      
# When Mother's height is constant 
print("1 inch change in dad's height -> {} inch change in son's height"\
      .format(round(regressor_OLS.params[1],2)))
