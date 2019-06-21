# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 16:13:19 2019

@author: Aditya Tanwar
"""

count=0
with open('absentee.txt', mode='wt') as file:
    while(count<15):
     name= input("Enter names=")
     count+=1
     file.write(name+'\n')
     if not name:
         break
     
if name =="":
    print("You entered nan value!")
else:
    with open('absentee.txt', mode='rt') as file:
        for line in file:
            name = file.readlines()
            print(name)
