# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 10:20:58 2019

@author: Aditya Tanwar
"""

user_input = input("Enter comma seperated Numbers: ").split(",")

user_list = [] #empty list

for i in user_input:
    user_list.append(int(i))

# Sorting
user_list.sort()

f_list = user_list[1:-1]
average = sum( f_list ) / len( f_list )

print ("Average is :", int( average ))