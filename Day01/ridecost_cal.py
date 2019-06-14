# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 17:34:21 2019

@author: Aditya Tanwar
"""

tot_travel=int(input("enter total traveled km "))
dl_cost=int(input("enter cost of disel/liter"))
average=int(input("enter the average "))
total_cost=(tot_travel/average)*dl_cost
print(total_cost)