# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 14:25:00 2022

@author: sebas
"""

age = int(input("Enter your age: "))
pre_hour=int(input("Per fortnight, how many hours you worked previously: "))
post_hour=int(input("How many hours you are currently working: "))
              





if age<24 and age>18 :
    total = (((pre_hour-post_hour )/pre_hour)*50)
    print(total)
    if total>40:
        print("you are elegible")
    else:
        print("you are not elegible")

elif age>24 :
    total = (((pre_hour-post_hour )/pre_hour)*100)
    print(total)
    print("you are elegible")
else:
    print("you are not elegible")
    
              