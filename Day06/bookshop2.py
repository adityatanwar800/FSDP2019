# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 10:43:10 2019

@author: Aditya Tanwar
"""


from functools import reduce

orders = [ [1, ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)], 
         [2, ("5464", 9, 9.99), ("9744", 9, 44.95)],
         [3, ("5464", 9, 9.99), ("88112", 11, 24.99)],
           [4, ("8732", 7, 11.99), ("7733",11,18.99), ("88112", 5, 39.95)] ]

min_order = 100

invoice_totals = list(map(lambda x: [x[0]] + list(map(lambda y: y[1]*y[2], x[1:])), orders))
print (invoice_totals)

invoice_totals = list(map(lambda x: [x[0]] + [round(reduce(lambda a,b: a + b, x[1:]),2)], invoice_totals))
print (invoice_totals)



from collections import OrderedDict

invoice = []
dict1 = OrderedDict()



orders = [ ['1', ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)], 
         ['2', ("5464", 9, 9.99), ("9744", 9, 44.95)],
         ['3', ("5464", 9, 9.99), ("88112", 11, 24.99)],
         ['4', ("8732", 7, 11.99), ("7733",11,18.99), ("88112", 5, 39.95)] ]


for newList in orders:
        orderNum = newList[0]
        info = (newList[1:])
        for new in info:
           invoice.append([orderNum,(list(new)[1] * list(new)[2])])
       
for new in invoice:
        dict1[new[0]] = dict1.get(new[0], 0) +  new[1] 
        #print(dict1)
        if(dict1[new[0]] < 100):
             print((new[0],dict1[new[0]]))
        else:
          print(dict1)  
    
