# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 16:14:51 2019

@author: Aditya Tanwar
"""


import pandas as pd


data = pd.read_csv('affairs.csv')  
data.head()

labels = data.iloc[:,8].values 
features = data.iloc[:,:-1].values



#one hot encoding
from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [6])
features = onehotencoder.fit_transform(features).toarray()

# dropping first column
features = features[:, 1:]


onehotencoder1 = OneHotEncoder(categorical_features = [-1])
features = onehotencoder1.fit_transform(features).toarray()

# dropping first column
features = features[:, 1:]

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.25, random_state = 0)


# Fitting Logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(features_train, labels_train)

#Calculate Class Probabilities
probability = classifier.predict_proba(features_test)

# Predicting the class labels
labels_pred = classifier.predict(features_test)

pd.DataFrame(labels_pred, labels_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)


