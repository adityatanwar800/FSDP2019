# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 09:39:48 2019

@author: Aditya Tanwar
"""


def bricks(small, big,target): #function define
    if target % 5 > small: #check for condition
        print (False) 
    else:    
        extract= big*5 + small
        if extract>= target:
            print (True)
        else:
            print (False)

list1 = input("Enter Numbers: ").split(",") #take input from user

flist=[] #make empty list

for i in list1:
    flist.append(int(i))
bricks(flist[0], flist[1], flist[2])