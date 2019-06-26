# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 16:00:27 2019

@author: Aditya Tanwar
"""

import numpy as np
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('University_data.csv')

#check for none value
dataset.isnull().any(axis=0)

#features and label
features = dataset.iloc[:, :-1].values
labels = dataset.iloc[:, -1].values

#label encoding
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
features[:, 0] = labelencoder.fit_transform(features[:, 0])

#onehotencoding
from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [0])
features = onehotencoder.fit_transform(features).toarray()

# dropping first column
features = features[:, 1:]

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2, random_state = 0)

# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train, labels_train)

print(regressor.intercept_)  
print (regressor.coef_)


# Predicting the Test set results
Pred = regressor.predict(features_test)
print(Pred)