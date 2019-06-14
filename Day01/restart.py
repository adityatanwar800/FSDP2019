# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 11:12:31 2019

@author: Aditya Tanwar
"""

string="restart"
str1=string.replace('r','$')
str2=str1.replace('$','r',1)
string1=string[1:]
str1=string1.replace('r','$')
print(string[0]+str1)