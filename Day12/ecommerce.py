# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 16:19:26 2019

@author: Aditya Tanwar
"""

import numpy as np 
import matplotlib.pyplot as plt
total_amt = np.random.normal(100.0, 20.0, 10000)

print (total_amt)

from scipy import stats
print("Mode value is: ", stats.mode(total_amt)[0])
print("Mean value is: ", np.mean(total_amt))
print("Median value is: ", np.median(total_amt))

plt.hist(total_amt, 20)
plt.xlabel("total amount")

# Setting the Y Label
plt.ylabel("transaction")

plt.title("E-commerce Data Exploration")

plt.boxplot(total_amt)
incomes = np.append(total_amt, [10000000])

plt.show()
