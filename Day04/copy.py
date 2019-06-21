# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 15:09:03 2019

@author: Aditya Tanwar
"""
with open('words.txt', mode='rt') as file:
    with open('copy.txt', mode='wt') as file_copy:
        for line in file:
            file_copy.write(line)
        