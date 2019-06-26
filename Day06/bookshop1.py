# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 10:23:35 2019

@author: Aditya Tanwar
"""

orders = [["34587", "Learning Python, Mark Lutz", 4, 40.95], 
              ["98762", "Programming Python, Mark Lutz", 5, 56.80], 
              ["77226", "Head First Python, Paul Barry", 3,32.95],
              ["88112", "Einführung in Python3, Bernd Klein",  3, 24.99]]
min_order = 100

order_summary = list(map(lambda x: (x[0], round(x[2] * x[3],2)), orders))
print(order_summary)

invoice_totals = list(map(lambda x: x if x[1] >= min_order else (x[0], x[1] + 10), order_summary))
print(invoice_totals)


invoice = []

orders = [ ["34587", "Learning Python, Mark Lutz", 4, 40.95], 
         ["98762", "Programming Python, Mark Lutz", 5, 56.80], 
           ["77226", "Head First Python, Paul Barry", 3,32.95],
           ["88112", "Einführung in Python3, Bernd Klein",  3, 24.99]]


for new in orders :
    orderNum = int(new[0])
    quantity = new[2]
    price = new[3]
    total = quantity * price
    if total<=100:
        total =total + 10
    else:
        total
    invoice.append((orderNum,total))  
    
print(invoice) 