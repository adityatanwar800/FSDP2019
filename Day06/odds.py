# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 10:56:17 2019

@author: Aditya Tanwar
"""

from functools import reduce
mylist = input().split(',')
def m_func(n):
    return int(n)
    
def f_func(x):
    return x%2 == 1

def r_func(x,y):
    return x*y

def productOfOdds(mylist):
    return reduce(r_func, filter(f_func, (map(m_func, mylist))))

print(productOfOdds(mylist))