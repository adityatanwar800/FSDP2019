# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 16:36:10 2019

@author: Aditya Tanwar
"""
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn import datasets
# import some data to play with
iris = datasets.load_iris()
features = iris.data  # we only take the first two features.
labels = iris.target



# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2, random_state = 0)

# Applying PCA
from sklearn.decomposition import PCA
pca = PCA(n_components = 2)
features = pca.fit_transform(features)


# Fitting Logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(features_train, labels_train)

# Predicting the Test set results
labels_pred = classifier.predict(features_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)

# Using the elbow method to find the optimal number of clusters
from sklearn.cluster import KMeans 

kmeans =KMeans(n_clusters = 3, init = 'k-means++', random_state = 0)
pred_cluster = kmeans.fit_predict(features)
setosa=features[pred_cluster == 0, 0]
virginica=features[pred_cluster == 1, 0]
versicolor=features[pred_cluster == 2, 0]


kmeans =KMeans(n_clusters = 3, init = 'k-means++', random_state = 0)
pred_cluster1 = kmeans.fit_predict(features)
plt.scatter(features[pred_cluster1 == 0, 0], features[pred_cluster1 == 0, 1], c = 'blue', label = 'setosa')
plt.scatter(features[pred_cluster1 == 1, 0], features[pred_cluster1 == 1, 1], c = 'red', label = 'virginica')
plt.scatter(features[pred_cluster1 == 2, 0], features[pred_cluster1 == 2, 1], c = 'green', label = 'versicolor')

plt.title('Clusters of datapoints')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()