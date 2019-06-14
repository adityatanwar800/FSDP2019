# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 10:09:50 2019

@author: Aditya Tanwar
"""


uinput = input("Enter comma seperated nos >").split(",")

pre_number_is_13 = False
sum = 0

for number in uinput:
    if int(number) == 13:
        pre_number_is_13 = True
    
    elif not pre_number_is_13:
        sum += int(number)
    
    elif pre_number_is_13 and int(number) != 13:
        pre_number_is_13 = False

print (sum)
