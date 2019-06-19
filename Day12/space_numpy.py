# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 15:49:57 2019

@author: Aditya Tanwar
"""
import numpy as np 
input_data =input("Enter a list element separated by space ")
x  = input_data.split()
x= np.array(x) 
print(type(x))
x=x.reshape(3,3)
print (x)
