# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 17:24:42 2019

@author: Aditya Tanwar
"""
names = ['Mary', 'Isla', 'Sam']
print (list(map(lambda names: hash(names) , names)))