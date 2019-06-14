# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 15:40:35 2019

@author: Aditya Tanwar
"""

import sqlite3
from pandas import DataFrame


# File based database ( connects if exits or creates a new one if it does not exists ) 
conn = sqlite3.connect ( 'db_niversity.db' )


# creating cursor
c = conn.cursor()

#c.execute("drop table employees")
# STEP 1
# www.sqlite.org/datatype3.html
c.execute ("""CREATE TABLE employees(
          student_name TEXT,
           Age INTEGER,
           roll_no INTEGER,
          branch TEXT
         
          )""")

# STEP 2
c.execute("INSERT INTO employees VALUES ('Sylvester',20,001, 'cs')")
c.execute("INSERT INTO employees VALUES ('yogendra',20,002, 'cs')")
c.execute("INSERT INTO employees VALUES ('Pradeep', 20,003, 'cs')")
c.execute("INSERT INTO employees VALUES ('Kunal', 20,004, 'cs')")
c.execute("INSERT INTO employees VALUES ('Devendra',20,005, 'cs')")
c.execute("INSERT INTO employees VALUES ('aditya',20,006, 'cs')")
c.execute("INSERT INTO employees VALUES ('himanshu',20,007, 'cs')")
c.execute("INSERT INTO employees VALUES ('lakshay', 20,008, 'cs')")
c.execute("INSERT INTO employees VALUES ('Kunal', 21,009, 'cs')")
c.execute("INSERT INTO employees VALUES ('abhishek',20,010, 'cs')")

c.execute("SELECT * FROM employees")
print ( c.fetchall() )
