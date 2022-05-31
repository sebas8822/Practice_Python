# -*- coding: utf-8 -*-
"""
Created on Tue May 31 17:39:37 2022

@author: sebas
"""

"""
The aim of this task is to create a list for storing student records.
 Consider a student record consists of following fields: *ID, Last Name, 
 First Name,* and *Marks.* Write a program that gets student data from the
 user and stores those as records in a list called `students`. You must 
 validate the marks input so that it only contains a number between 0 and 100.
 In the beginning, the program should also prompt the user for the number
 of student records.

**Note:** The student list will have a 
structure like this:
    `['123', 'Lu', 'Kevin', 85.0, '429', 'Jane', 'Mary', 60.0, ...]` 
    (four elements per student)
"""


def main():
    
    students = []
    
    std_records = int(input("How many student records? ->"))
    count = 1
    
    for i in range(0,std_records):
        print('*** Student #' + str(count) + ' ***')
        std_id = input_ID()
        students.append(std_id)
        #ID = random.randint(100,999)
        Last_Name = "LAST" + str(std_id)
        students.append(Last_Name)
        First_Name = "Name"+ str(std_id)
        students.append(First_Name)
        Marks = marks_input()  
        students.append(Marks)
        count+=1
        
    print_list(students)
    
 
    
        
def input_ID():
    
    valid = False
    while not valid:
        try:
            input_user = int(input('Enter value of 3 digit: '))
        except ValueError:  # catch not integer inputs
            print('Student ID should be numeric. Try again')
        else:  # if no exception (integer input)
            valid = True

    return input_user
    
    
    
    
        
def marks_input():
    valid  = False
    
    while not valid:
        try:
            value = float(input("Please insert the mark"))          

        except ValueError:
            print("Value should be numeric input")
        else:
            if value >= 0 and value <= 100:
                valid = True
            else:
                print("Value should be numeric between 0-100")
            
            
    return value

def print_list(list_std):
    
    
    print('-----------------------------------')
    print('ID   Last Name   First Name   Mark')
    print('-----------------------------------')
    
    for i in range(0,len(list_std),4):
        
        sid = str(list_std[i])
        last_name = str(list_std[i+1])
        first_name = str(list_std[i+2])
        mark = float(list_std[i+3])
        print(f'{sid:5s}{last_name:12s}{first_name:13s}{mark}')
    
   
            
            
        
            
    
main()





















