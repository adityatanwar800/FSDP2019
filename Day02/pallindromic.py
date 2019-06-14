# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 09:39:48 2019

@author: Aditya Tanwar
"""

uinput = input("Enter space seperated values :").split()

input_len  = len(uinput)
count = 0
pallindromic_integer = False

for number in uinput:
    if int(number) > 0:
        count += 1

if count == input_len:
    for positive_num in uinput:
        if positive_num == positive_num[::-1]:
            pallindromic_integer = True
            
print(pallindromic_integer)

    