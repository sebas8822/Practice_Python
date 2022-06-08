# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 14:47:20 2022

@author: sebas
"""

def fuelBurn(minutes):
    min_sec = minutes*60
    comsumed_fuel = 11000*min_sec
    return (comsumed_fuel/22046)*100

def main():
    
    print('-----------------------------------')
    print('Time (Min)   |Fuel Consumed(Kg)')
    print('-----------------------------------')
    
    for i in range(2,10+1,2):
        print("\t\t" + str(i) + "\t|\t"+ str(format(fuelBurn(i),'.3f')) )
    
main() 
