# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 16:46:14 2019

@author: Aditya Tanwar
"""

spr_mkt={}

while True:
  item= input("Enter item >")
  if not item:
        break
    
  In_item=item.split()
  item_name=' '.join(In_item[:-1])
  item_price=In_item[-1]
  
  if item_name not in spr_mkt:
      spr_mkt[item_name]=item_price
  else:
      spr_mkt[item_name]=int(spr_mkt[item_name])+int(item_price)
print(list(spr_mkt.items()))      
  
  
  
  