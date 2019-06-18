# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 16:29:15 2019

@author: Aditya Tanwar
"""
import matplotlib

from matplotlib import pyplot as plt
girls_grades = [89, 90, 70, 89, 100, 80, 90, 100, 80, 34]
boys_grades = [30, 29, 49, 48, 100, 48, 38, 45, 20, 30]
grades_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# For Plotting Scatter Plot


# Showing the points on the graph
plt.scatter(grades_range, girls_grades)
plt.scatter(grades_range, boys_grades)
#plt.scatter(x, y, marker='o')

# Scatter Plot with scatter method 
# o  .  , x  +  v  ^  <  >  s d 
plt.scatter(grades_range, girls_grades, marker='.', color='black',label="marker='{0}'".format('.')); 
plt.scatter(grades_range, boys_grades, marker='o', color='green',label="marker='{0}'".format('.')); 


plt.show()
