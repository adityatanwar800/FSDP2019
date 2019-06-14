# -*
- coding: utf-8 -*-
"""
Created on Thu Jun 13 16:40:33 2019

@author: Aditya Tanwar
"""

from  selenium import webdriver
from time import sleep

url = "https://bidplus.gem.gov.in/bidlists"

browser = webdriver.Chrome("C:\\Users\\Aditya Tanwar\\Downloads\\chromedriver_win32\\chromedriver.exe")
browser.get(url)

sleep(3)
32/*

import mysql.connector 
# connect to  MySQL server along with Database name
conn = mysql.connector.connect(user='adityat', password='aditya@123', host='db4free.net', database = 'adityabid')
# creating cursor
c = conn.cursor()
# creating table
c.execute ("""CREATE TABLE bid_plus(
             bid_num TEXT,
             items TEXT,
             quantity_req INTEGER,
             dept_details TEXT,
             start_date TEXT,
             start_time TEXT,
             end_date TEXT,
             end_time TEXT
          )""")
conn.commit()

for i in range(1,11):
    
    bid_num = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[1]/p[1]/a').text.replace("\n"," ")
    
    items = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[1]/span').text.replace("\n"," ")
    
    quantity_req = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[2]/span').text.replace("\n"," ")
    
    dept_details = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[3]/p[2]').text.replace("\n"," ")
    
    start_date = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[1]/span').text[:10]
    
    start_time = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[1]/span').text[11:]
    
    end_date = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[2]/span').text[:10]
    
    end_time = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[2]/span').text[11:]
    
    # to store data into database
    c.execute("INSERT INTO bid_plus VALUES('{}','{}',{},'{}','{}','{}','{}','{}')".format(bid_num,items,int(quantity_req),dept_details,start_date,start_time,end_date,end_time))
    conn.commit()

# Retriving data from database
c.execute("SELECT * FROM bid_plus")
from pandas import DataFrame
df = DataFrame(c.fetchall())  
df.columns = ["Bid Number","Items","Quantity Required","Department Name and Address","Start Date","Start Time","End Date","End Time"]