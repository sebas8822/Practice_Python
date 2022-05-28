# -*- coding: utf-8 -*-
"""
Created on Fri May 27 15:21:41 2022

@author: sebas
"""

"""
Write a program to create a data file for storing student records.
 Assume a student record consists of the following fields: ID, Last Name,
 First Name, and Marks. The Marks field contains a number between 0 and 100.
 Write a program that loops to get data for multiple students from the user
 and stores those as records in the student.txt file. The user should enter 
 a negative number as the ID to signal the end of the loop. Your program 
 should be able to reject non-numeric and out of range marks. Additionally,
 handle all file related exceptions.
"""


dict1 = {}
# createa  a file and how it will be created to hold the data 
student_file = open('student.txt','w') # automatically creates the file if it does not exits

def main():
    ID = id_input()    
    
    while ID != -1:
    
        #ID = random.randint(100,999)
        student_file.write(str(ID)+", ")
        Last_Name = "LAST" + str(ID)
        student_file.write(Last_Name+", ")
        First_Name = "Name"+ str(ID)
        student_file.write(First_Name + ", ")
        Marks = marks_input()
        student_file.write(str(Marks) + "\n")
        
        ID = id_input()
    student_file.close()
    
    
def marks_input():
    valid = False
    msg = 'Mark can only be a decimal number 0 to 100. Try again'
    while not valid:
        try:
            mark = float(input('Enter student marks: '))
            if 0 <= mark <= 100:
                valid = True
            else:
                print(msg)
        except ValueError:
            print(msg)

    return mark


def id_input():
    valid = False
    while not valid:
        try:
            sid = int(input('Enter student ID (-1 value to finish): '))
        except ValueError:  # catch not integer inputs
            print('Student ID should be numeric. Try again')
        else:  # if no exception (integer input)
            valid = True

    return sid


main()




