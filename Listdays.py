# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 10:08:02 2022

@author: sebas
"""
#                           -4   -3    -2    -1
days = ["Mon","Tue","Wen","Thu","Fri","Sat","Sun"]

# for i in days:
#     print(i.lower())
    
print(days[6]) #error the list just contains 7 elements
print(days[5:10]) # retrive just the elements 5 to 7 because there are not more elements
print(days[:-4])# Python allow negative index where the last element is -1 so the slicing retrive the elements -5-6-7



days = days[6:] + days[:5]
print(days)