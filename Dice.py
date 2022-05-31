# -*- coding: utf-8 -*-
"""
Created on Tue May 31 17:04:58 2022

@author: sebas

Write a program that rolls a dice several times as specified by the user. 
The program should contain a roll function with an integer parameter
 number_of_rolls. The function simulates a dice roll 
 (generates a random number 1 to 6) and appends the result to a list.
 Upon completing number_of_rolls iterations, the list must be returned 
 back to the main function which displays the list. If the user enters 
 10 rolls, the program will show a list of 10 dice roll results.
"""

import random


def main():
    # ask to the user how many times roll the dice
    rolls = count_input() 
    
    print("Results\n", roll(rolls))


def count_input():
    valid = False
    while not valid:
        try:
            count = int(input('How many times you want to roll the dice? '))
        except ValueError:
            print('Please use numeric input')
        else:
            valid = True

    return count

def roll(number_of_rolls):
    
    rolls = []
    for i in range(0,number_of_rolls):
        rolls.append(random.randint(1, 6))
    return rolls


main()
    
    

