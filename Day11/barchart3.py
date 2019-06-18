# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 15:40:23 2019

@author: Aditya Tanwar
"""


import matplotlib

from matplotlib import pyplot as plt

ages_x = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
          36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]

Developer = [17784, 16500, 18012, 20628, 25206, 30252, 34368, 38496, 42000, 46752, 
49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752, 77232,
78000, 78508, 79536, 82488, 88935, 90000, 90056, 95000, 90000, 91633, 91660, 
98150, 98964, 100000, 98988, 100000, 108923, 105000, 103117]

python=[20046, 17100, 20000, 24744, 30500, 37732, 41247, 45372, 48876, 53850, 
57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640, 84666,
84392, 78254, 85000, 87038, 91991, 100000, 94796, 97962, 93302, 99240, 102736, 
112285, 100771, 104708, 108423, 101407, 112542, 122870, 120000]

java_script=[16446, 16791, 18942, 21780, 25704, 29000, 34372, 37810, 43515, 46823, 
49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583, 79000,
78508, 79996, 80403, 83820, 88833, 91660, 87892, 96243, 90000, 99313, 91660, 
102264, 100000, 100000, 91660, 99240, 108000, 105000, 104000]
'''
plt.bar(ages_x,Developer,label="Developer")
plt.bar(ages_x,python,label="python")
plt.bar(ages_x,java_script,label="java_script")
'''

plt.xlabel("Ages")

# Setting the Y Label
plt.ylabel("Median Salary (USD)")
width = .40
dev_1 = [i-width/3 for i in ages_x]
dev_2=[i+width/3 for i in ages_x]
plt.title("Median Salary (USD) by Age")
plt.bar(dev_1,Developer, width/3, alpha=1.0)
plt.bar(ages_x,python, width/3, alpha=1.0)
plt.bar(dev_2,java_script, width/3, alpha=1.0)
"""
plt.bar(ages_x, Developer, color='green') # #000000    k is for black
plt.bart(ages_x,python , color='blue')
plt.bar(ages_x, java_script, color='red')

# Changing the marker of the line

plt.plot(ages_x,Developer, marker='X') 
plt.plot(ages_x,python, marker='o') 
plt.plot(ages_x,java_script, marker='+') 
                     
# Changing the color of the line
plt.plot(ages_x, Developer, color='green') # #000000    k is for black
plt.plot(ages_x,python , color='blue')
plt.plot(ages_x, java_script, color='red')

# Changing the style of the line
#plt.plot(x, y, linestyle='dashed') # solid dashed  dashdot dotted
                                   # -- -. - 

# Changing the width of the line
#plt.plot(x, y, linewidth=5) 
"""

plt.show()


