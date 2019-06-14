# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 16:48:03 2019

@author: Aditya Tanwar
"""
year=int(input("enter the year to find the leap year or not>"))
def leap_year(year):
    if year%4==0 and year%100!=0 or year%400==0:
        return 'True'
    else:
        return 'False'   
leap_year(year)
