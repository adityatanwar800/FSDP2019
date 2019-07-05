# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 11:30:49 2019

@author: Aditya Tanwar
"""


# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#import dataset
dataset = pd.read_csv('tshirts.csv')
features = dataset.iloc[:,1: ].values
#Scatter all these data points on the matplotlib
plt.scatter(features[:,0], features[:,1])
plt.show()

from sklearn.cluster import KMeans 

kmeans =KMeans(n_clusters = 3, init = 'k-means++', random_state = 0)
pred_cluster1 = kmeans.fit_predict(features)
plt.scatter(features[pred_cluster1 == 0, 0], features[pred_cluster1 == 0, 1], c = 'blue', label = 'small')
plt.scatter(features[pred_cluster1 == 1, 0], features[pred_cluster1 == 1, 1], c = 'red', label = 'medium')
plt.scatter(features[pred_cluster1 == 2, 0], features[pred_cluster1 == 2, 1], c = 'green', label = 'large')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')
plt.title('Clusters of datapoints')
plt.xlabel('height')
plt.ylabel('weight')
plt.legend()
plt.show()

#size std
small=kmeans.cluster_centers_[2]
medium=kmeans.cluster_centers_[0]
large=kmeans.cluster_centers_[1]
