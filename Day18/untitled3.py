# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 15:59:13 2019

@author: Aditya Tanwar
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 16:32:34 2019

@author: Aditya Tanwar
"""

import numpy as np
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('iq_size.csv')

#check for none value
dataset.isnull().any(axis=0)

#features and label
features = dataset.iloc[:,1:].values
labels = dataset.iloc[:,0 ].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2, random_state = 0)


# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train, labels_train)



x = [90,70,150]
x = np.array(x)
regressor.predict(x.reshape(1, 3))

import statsmodels.api as sm
features = sm.add_constant(features)


features_opt = features[:, [0, 1, 2, 3]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()

features_opt = features[:, [0, 1, 2]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()