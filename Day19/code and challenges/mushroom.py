# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 17:58:02 2019

@author: Aditya Tanwar
"""

import pandas as pd
data2 = pd.read_csv('mushrooms.csv', sep=',', header=0)  

labels = data2.iloc[:, 0].values 
features = data2.iloc[:, 21:]
features['odor']= data2['odor']
features=features.values
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
features[:, 0] = labelencoder.fit_transform(features[:, 0])
features[:, 1] = labelencoder.fit_transform(features[:, 1])
features[:, 2] = labelencoder.fit_transform(features[:, 2])

from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [0])
features = onehotencoder.fit_transform(features).toarray()
features = features[:, 1:]

onehotencoder1 = OneHotEncoder(categorical_features = [5])
features = onehotencoder1.fit_transform(features).toarray()
features = features[:, 1:]

onehotencoder2 = OneHotEncoder(categorical_features = [11])
features = onehotencoder2.fit_transform(features).toarray()
features = features[:, 1:]

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.25, random_state = 0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(features_train, labels_train)
probability = classifier.predict_proba(features_test)
labels_pred = classifier.predict(features_test)
pd.DataFrame(labels_pred, labels_test)