# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 10:10:58 2019

@author: Aditya Tanwar
"""

std_list = []

while True:
    u_input = input("Enter name, age and score: ")
    
    if not u_input:
        break  
    name, age, marks = u_input.split(",")
    std_list.append( (name, int(age), int(marks) ) )

std_list.sort()
print (std_list)
