# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 16:45:30 2019

@author: Aditya Tanwar
"""
import csv
import matplotlib

from matplotlib import pyplot as plt
year=[]
level=[]

with open('sealevel.csv','rt') as ani:
    reader = csv.reader(ani)
    next(reader)
    for row in reader:
        print(row)
# split dictionary into keys and values 
        year.append(int(row[0])) 
        level.append(float(row[1])) 
print(year)
print(level)        
plt.plot(year,level)

plt.xlabel("years")

# Setting the Y Label
plt.ylabel("sea_level_rises(inches)")

plt.title("sea level rises per year")
plt.legend()
plt.show()

    