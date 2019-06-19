# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 16:30:30 2019

@author: Aditya Tanwar
"""

import numpy as np
                           #mean, sd, total
incomes = np.random.normal(150, 20, 1000)
import matplotlib.pyplot as plt
plt.hist(incomes, 100)
plt.show()
from scipy import stats
print("Mode value is: ", stats.mode(incomes)[0])
print("Mean value is: ", np.mean(incomes))
print("Median value is: ", np.median(incomes))