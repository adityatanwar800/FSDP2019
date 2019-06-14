# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 15:56:49 2019

@author: Aditya Tanwar
"""
  


"""
Database handling using MongoDB on Cloud -  Mongo Atlas
"""


import pymongo
import dns
#import dns # required for connecting with SRV

#client = pymongo.MongoClient("mongodb://K_Vaid:123chandu30%26@cluster0-shard-00-00-tofyu.mongodb.net:27017,cluster0-shard-00-01-tofyu.mongodb.net:27017,cluster0-shard-00-02-tofyu.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
client = pymongo.MongoClient("mongodb://aditya:%40123@cluster0-shard-00-00-ks1sy.mongodb.net:27017,cluster0-shard-00-01-ks1sy.mongodb.net:27017,cluster0-shard-00-02-ks1sy.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")


mydb = client.db_university

def add_employee(name,age,roll,branch):
    #unique_employee = mydb.employees.find_one({"id":idd})
    #if unique_employee:
    #    return "Employee already exists"
    #else:
    mydb.employees.insert_one(
            {
            "student_name" :name,
             "age":age,
           "roll_no":roll, 
            "branch":branch
            })
    return "Employee added successfully"


def fetch_all_employee():
    user = mydb.employees.find()
    for i in user:
        print (i)




add_employee('Sylvester',20,1,'cs')
add_employee ('yogendra',20,2, 'cs')
add_employee('Pradeep', 20,3, 'cs')
add_employee ('Kunal', 20,4, 'cs')
add_employee ('Devendra',20,5, 'cs')
add_employee('aditya',20,6, 'cs')
add_employee ('himanshu',20,7, 'cs')
add_employee('lakshay', 20,8, 'cs')
add_employee ('Kunal', 21,9, 'cs')
add_employee('abhishek',20,10, 'cs')

fetch_all_employee()



#
#client = pymongo.MongoClient("mongodb://aditya:<password>@cluster0-shard-00-00-ks1sy.mongodb.net:27017,cluster0-shard-00-01-ks1sy.mongodb.net:27017,cluster0-shard-00-02-ks1sy.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
#db = client.test
