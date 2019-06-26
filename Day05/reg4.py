# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 11:50:51 2019

@author: Aditya Tanwar
"""
import re
email_list= list()

while True:
    email= input("Enter email=")
    if not email:
        break
    email_list.append(email)

valid=[]
for email in email_list:
    if re.match(r'^[a-z0-9_-]+@[a-z0-9_-]+.[a-z-]{2,4}$',email):
        valid.append(email)

print("Valid email:", (valid))