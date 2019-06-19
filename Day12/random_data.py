# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 15:49:58 2019

@author: Aditya Tanwar
"""

import numpy as np 
x = np.random.randint(5,15,40)

print (x)
from scipy import stats
print("Mode value is: ", stats.mode(x)[0])