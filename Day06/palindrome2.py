# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:07:55 2019

@author: Aditya Tanwar
"""

print(any(map(lambda i: True if str(i) ==str(i)[::-1] and i>0 else False ,map(int,input('Enter numbers>').split(',')))))


