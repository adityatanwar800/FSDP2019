# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 17:04:19 2019

@author: Aditya Tanwar
"""
month=input("enter the month>")
def day_in_month(month):
    if month in ("january","march","may","july","august","october","december"):
        return "31"
    elif month == "febuary":
        return "27 or 28"
    else:
        return "30"
day_in_month(month)
    
        
    