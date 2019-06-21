# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 17:02:01 2019

@author: Lakshya
"""

with open('words.txt', mode='rt') as file :
   file_contents = file.readlines()
   print (file_contents[-1])