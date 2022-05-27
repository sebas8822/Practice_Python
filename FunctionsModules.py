# -*- coding: utf-8 -*-
"""
Created on Thu May 26 11:29:08 2022

@author: sebas
"""


"""
**Currency converter program**

Write a program that will generate and print N random values where each 
value can vary between 1 and 100. At the end, the program should also
 display the number of odd values and even values generated.
 For example, if N=10 and if the 
 program generates 5, 48, 73, 29, 33, 99, 44, 45, 78 and 88 
 then it will report odd values = 6 and even values = 4. 
 You should use at least one value returning function in your program.
 
"""
'''
def main():
   my_ramVal=  random_val(10)  
   print(my_ramVal)
   print("Odds: ",odd(my_ramVal))
   print("Evens: ",even(my_ramVal))
   
def random_val(N):
    ram_num = []
    import random
    for i in range(1,N+1):
        ram_num.append(random.randint(0, 100))
    return ram_num
def odd(listN):
    #list_odds = []
    num_odds = 0
    for i in listN:
        if(i % 2 == 1):
            #list_odds.append(i)
            num_odds = num_odds + 1
    return num_odds#list_odds
def even(listN):
    #list_odds = []
    num_evens = 0
    for i in listN:
        if(i % 2 == 0):
            #list_odds.append(i)
            num_evens = num_evens + 1
    return num_evens#list_odds


   
main()
'''

"""
Write a function called `is_prime` that takes in a positive integer 
as argument and returns a Boolean to indicate if the number is prime or not.
 A simple algorithm for prime checking is given below. Test the function 
 by calling it from `main`.
 Let us say we want to check 83. Start from the number 2 and check
 if 83 is divisible by 2 (use remainder operator: `%`).
 If not divisible by 2, move to next divisor, 
 3. If divisible by 3, stop and report the number as non-prime.
 Otherwise continue checking with the next divisors 4, 5, 6… . 
 If the divisor value exceeds the square root of 83, stop iterating 
 and report the number as prime.
"""
'''
def is_prime(N):
    flag = False
    if N > 1:
        for i in range(2,N):
            if (N % i == 0):
                flag = True
                break
    if flag:
        return False
    else:
        return True

def main():
     
   
    for i in range(0,100):
        print("Number "+ str(i) + " is prime: " + str(is_prime(i)))
   
main()

'''
"""
Write a module called ‘customer.py’ which will have a function called 
calculate_points(). The function will take an input called total_purchases
 as a parameter and return the loyalty points earned by a customer. 
 The points are calculated based on the total purchases (rounded figure)
 according to the following table.
 """
'''
def calculate_points(total_purchases):
    points = 0
    if total_purchases > 0 and total_purchases < 100:
        points+=10
        
    if total_purchases > 100 and total_purchases < 500:
        points+=20
    
    if total_purchases > 500:
        points+=20

        
    return points
    

def main():
     
   print(calculate_points(200))
   
main()
'''

"""
Write a program to implement the rock, paper, scissors game.
 Assume rock, paper and scissors are represented
 by values 1, 2 and 3 respectively. When the program starts,
 the computer should randomly choose a move and then prompt
 the user for their move (1 to 3). Then the program should 
 compare the two moves and choose the winner according to the 
 [rules of the game]
 (https://upload.wikimedia.org/wikipedia/commons/6/67/Rock-paper-scissors.svg).
 This completes one round of the game. Then the program should prompt the user 
 if they would like to play another round.
 
    Apply top down decomposition to use several functions in this program,
    such as a function to accept user's move, a function to work out the 
    round winner, a function to prompt the user for continuing etc.
    
    def play1(user_input):
    
    
    
    machine = random.randint(1, 3)
    
    if (user_input == machine):
            print ("User: " + define(user_input),
                   "\nMachine: " + define(machine) + " \ndraw!! ")
            
            
    elif (user_input == 1 and machine == 2):
            print ("User: " + define(user_input),
                   "\nMachine: " + define(machine) +  " \nmachine win!! ")
    elif (user_input == 2 and machine == 1):
            print ("User: " + define(user_input),
                   "\nMachine: " + define(machine) + " \nUser win !! ")
            
    elif (user_input == 2 and machine == 3):
            print ("User: " + define(user_input),
                   "\nMachine: " + define(machine) + " \nmachine win!! ")
    elif (user_input == 3 and machine == 2):
            print ("User: " + define(user_input),
                   "\nMachine: " + define(machine) + " \nUser win!! ")
    
    elif (user_input == 3 and machine == 1):
            print ("User: " + define(user_input),
                   "\nMachine: " + define(machine) + " \nmachine win!! ")
    elif (user_input == 1 and machine == 3):
            print ("User: " + define(user_input),
                   "\nMachine: " + define(machine) + " \nUser win!! ")
    
    
    return machine

"""
'''

import random



def main():
    
    user_input = int(input("Insert (-1) for exit\n - rock(1)\n - paper(2)\n - scissors(3)\nOPTION-->")) 
    while user_input!=-1 :
         print(play2(user_input))
         user_input = int(input("Insert (-1) for exit\n - rock(1)\n - paper(2)\n - scissors(3)\nOPTION-->")) 
    
    
def define(option):
    if option == 1:
        return "rock"
    if option == 2:
        return "paper"
    if option == 3:
        return "scissors"
        

def play2(user_input):
    listO = [1,2,3]
    machine = random.randint(1, 3)
    
    if (user_input == machine):
            return "User: " + define(user_input) + "\nMachine: " + define(machine) + " \ndraw!! "
    elif listO[listO.index(machine)-2 ] == user_input  :
            return "User: " + define(user_input) + "\nMachine: " + define(machine) + " \nUser win!! "
    else:
            return "User: " + define(user_input) + "\nMachine: " + define(machine) + " \nmachine win!! "
    
    
    
    
    
    
main()    


'''


















































