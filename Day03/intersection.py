# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 18:16:29 2019

@author: Aditya Tanwar
"""

lst1=input("enter the value").split()
set1=set(lst1)
lst2=input("enter the value for set 2").split()
set2=set(lst2)
set3=set1.intersection(set2) 
lst=list(set3)
print(lst)