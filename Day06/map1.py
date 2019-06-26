# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 17:03:55 2019

@author: Aditya Tanwar
"""

import random

names = ['Mary', 'Isla', 'Sam']
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']

print (list(map(lambda names: random.choice(code_names),names)))