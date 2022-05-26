# -*- coding: utf-8 -*-
"""
Created on Wed May 25 13:37:10 2022

@author: sebas
Write a program to find the middle of three numbers. 
The program should ask a user to enter three numbers
 which should be stored into three variables namely A, B and C.
 The program then finds and displays the middle number.
"""


flag = 0

A  = int(input("A->"))
B  = int(input("B->"))
C  = int(input("C->"))

if (A>B):
    if (A<C):
        print("A is the midle")
    else: 
     print("C is the midle")
if (A>C):
    print("A is the midle")
else:
     print("B is the midle")
    


