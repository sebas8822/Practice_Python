# -*- coding: utf-8 -*-
"""
Created on Tue May 31 21:25:57 2022

@author: sebas
"""

   
 
    
 # -*- coding: utf-8 -*-
"""
Created on Tue May 31 17:39:37 2022

@author: sebas
"""

"""
Extend the program in the task 2 to display details of all students
 scoring HD (85+) marks. You must use slicing operations to extract 
 information of a student from the full list.
"""
import random

def main():
    
    students = []
    
    std_records = int(input("How many student records? ->"))
    count = 1
    
    for i in range(0,std_records):
        print('*** Student #' + str(count) + ' ***')
        std_id = random.randint(100,999)        #input_ID()
        students.append(std_id)
        #ID = random.randint(100,999)
        Last_Name = "LAST" + str(std_id)
        students.append(Last_Name)
        First_Name = "Name"+ str(std_id)
        students.append(First_Name)
        Marks = random.randint(0,100)         #marks_input()  
        students.append(Marks)
        count+=1
        
        
    print(students)
        
    print_list(students)
    print_list(hd_students(students))
    
    
    
def hd_students(list_std):
    hd_std = []
    
    for i in range(0,len(list_std),4):
        
        
      if float(list_std[i+3])>=85:
          sid = str(list_std[i])
          hd_std.append(sid)
          last_name = str(list_std[i+1])
          hd_std.append(last_name)
          first_name = str(list_std[i+2])
          hd_std.append(first_name)
          mark = float(list_std[i+3])
          hd_std.append(mark)
          print(list_std[i:i+4])
      
    return hd_std
        
    
        
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





















  