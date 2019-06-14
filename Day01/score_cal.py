# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 17:41:44 2019

@author: Aditya Tanwar
"""

assig_01=int(input("enter score "))
assig_02=int(input("enter score "))
assig_03=int(input("enter score "))
exam_01=int(input("enter score "))
exam_02=int(input("enter score "))
total_weighted_score = ( assig_01+assig_02+assig_03 ) *0.1 + (exam_01 + exam_02 ) * 0.35
print(total_weighted_score)