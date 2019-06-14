# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 17:19:38 2019

@author: Aditya Tanwar
"""

state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']
f_fin=[]
vow=["a","i","o","u","e","A","E","O","I","U"]
index=0
for number in state_name:
    lst=list(number)
    final=[]
    for l in lst:
        if l not in vow:
            final.append(l)
    f_fin.append("".join(final))
print(f_fin)
