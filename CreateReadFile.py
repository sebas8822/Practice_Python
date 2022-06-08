# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 10:55:16 2022

@author: sebas
"""

hfile = open('hello.txt', 'r')
#hfile.write('treat each other \nwith respect.')


some_var = hfile.read()
print(len(some_var.split(' ')))
print(some_var.find('ea'))



hfile.close()