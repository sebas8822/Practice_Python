# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 10:55:12 2022

@author: sebas
"""

goals = {"Bican":805,"Romario":772,"Pele":767}

for key in goals:
    if goals[key]<800:
        print(key)