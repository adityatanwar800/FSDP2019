# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 10:56:18 2019

@author: Aditya Tanwar
"""


# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#import dataset
dataset = pd.read_csv('deliveryfleet.csv')
features = dataset.iloc[:,1: ].values
#Scatter all these data points on the matplotlib
plt.scatter(features[:,0], features[:,1])
plt.show()

# Using the elbow method to find the optimal number of clusters
from sklearn.cluster import KMeans 

kmeans =KMeans(n_clusters = 2, init = 'k-means++', random_state = 0)
pred_cluster = kmeans.fit_predict(features)
urban_driver=features[pred_cluster == 0, 0]
rural_driver=features[pred_cluster == 1, 0]


kmeans =KMeans(n_clusters = 4, init = 'k-means++', random_state = 0)
pred_cluster1 = kmeans.fit_predict(features)
plt.scatter(features[pred_cluster1 == 0, 0], features[pred_cluster1 == 0, 1], c = 'blue', label = 'urban_speed_follower')
plt.scatter(features[pred_cluster1 == 1, 0], features[pred_cluster1 == 1, 1], c = 'red', label = 'rural_speed_follower')
plt.scatter(features[pred_cluster1 == 2, 0], features[pred_cluster1 == 2, 1], c = 'green', label = 'urban_speed_unfollower')
plt.scatter(features[pred_cluster1 == 3, 0], features[pred_cluster1 == 3, 1], c = 'black', label = 'urban_speed_unfollower')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')
plt.title('Clusters of datapoints')
plt.xlabel('Dist')
plt.ylabel('speed')
plt.legend()
plt.show()
