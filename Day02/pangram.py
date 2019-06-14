# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 10:25:39 2019

@author: Aditya Tanwar
"""

inp_str = input("Enter the string :")
count = 0
list1 = []
lower_str = inp_str.lower()
for alpha in lower_str:
    list1.append(alpha)

f_list = []    

for number in list1: 
 if number not in f_list: 
  f_list.append(number) 
    
for elements in f_list:
    if elements in 'abcdefghijklmnopqrstuvwxyz':
        count += 1
if count == 26:
    print ("Pangram")
else:
    print ("Not Pangram")