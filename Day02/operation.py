# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 10:14:54 2019

@author: Aditya Tanwar
"""


def Add(lst):
    total = 0
    for i in lst:
        total += i
    return total

def Multiply(lst):
    product = 1
    for i in lst:
        product *= i
    return product

def Largest(lst):
    init = lst[0]
    for i in lst:
        if init < i:
            init = i
    return init

def Smallest(lst):
    init = lst[0]
    for i in lst:
        if init > i:
            init = i
    return init

def Sorting(lst):
    s = len(lst)
    us = True
    while us:
        us = False
        i = 0
        while i<s-1:
            if lst[i] > lst[i+1]:
                t = lst[i]
                lst[i] = lst[i+1]
                lst[i+1] = t
                us = True
            i += 1
    return lst

def Remove_Duplicates(lst):
    n_lst = []
    for i in lst:
        if i not in n_lst:
            n_lst.append(i)
    return n_lst

def Print(lst):
    lst = list(lst)
    print (Add(lst))
    print (Multiply(lst))
    print (Largest(lst))
    print (Smallest(lst))
    print (Sorting(lst))
    print (Remove_Duplicates(lst))

my_list = input("Enter list: ").split(",")

final_list = []

for i in my_list:
    final_list.append(int(i))
    
Print (final_list)
