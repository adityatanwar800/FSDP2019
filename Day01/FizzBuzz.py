# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 11:32:22 2019

@author: Aditya Tanwar
"""

num=0
while(num<100):
    num=num+1
    if(num%3==0 and num%5==0):
        print("FizzBuzz")
    elif(num%3==0):
     print("Fizz")
    elif(num%5==0):
     print("Buzz")
    else:
     print(num)