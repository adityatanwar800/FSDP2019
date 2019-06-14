# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 10:08:34 2019

@author: Aditya Tanwar
"""

def translate(string):
    
    vowels="aieouAEIOU"
    list1 = []

    for element in string:
        
       if element not in vowels:       
           list1.append(element+"o"+element)           
       else:
                 list1.append(element)

    return "".join(list1)

user_input = input("Enter string to translate: ")

print (translate(user_input))