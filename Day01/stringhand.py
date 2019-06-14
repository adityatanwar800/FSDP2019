# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 18:45:28 2019

@author: Aditya Tanwar
"""

newstr=input("enter the string: ")
index=newstr.find(' ')
print(newstr[index:] + " " + newstr[:index] )