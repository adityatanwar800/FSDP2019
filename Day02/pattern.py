# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 18:07:20 2019

@author: Aditya Tanwar
"""

def pattern(num):
    for i in range(0,num):
        print('*'*i)
    for i in range(num,0,-1):
        print('*'*i)
num=int(input("Enter a number>"))
print(num)
pattern(num)
