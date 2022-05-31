# -*- coding: utf-8 -*-
"""
Created on Sun May 29 11:46:19 2022

@author: sebas
"""

"""
Write a program to delete a specific student record from ‘students.txt’ 
data file (containing the same record structure as exercise 1). 
The program will prompt the user to enter a student ID. The program then
 searches the file for the given student ID, and if found, it displays the
 student record and then deletes the record from the file. If the ID is not
 found, then the program should display an informative message. Your program
 should handle all file I/O exceptions.
 """
 
import os  # Needed for deleting and renaming files


def main():
    deleted = False
    
    
    try:
        show_file('student.txt')
        #Read the file 
        std_file = open('student.txt', 'r')
        
        temp = open('temp.txt', 'w')
        
        
        
        sid = std_file.readline()
        
        delete_id = int(input("Please insert the id to delete "))
        # to delete a line we have to create a new file witht he data we need
        # this measns we are going to move to a temp file the data except for the 
        # one need to be deleted
        while sid != '':
            last_name = std_file.readline()
            first_name = std_file.readline()
            mark = std_file.readline()
    
            # Write all student information to tmp file, except for the deleted student
            if int(sid.rstrip()) != delete_id:
                temp.write(sid)  # All four variables already include a line break
                temp.write(last_name)
                temp.write(first_name)
                temp.write(mark)
            else:
                deleted = True  # so that later we know to rename the tmp file
                print('The following information has been deleted from the student data file.')
                print(sid.rstrip() + '\t' + last_name.rstrip() + '\t' + first_name.rstrip() + '\t' + mark.rstrip())
            
            # Get id of the next student
            sid = std_file.readline()
        
        std_file.close()
        temp.close()
        
        if deleted:# flag if it is true
        
        # Delete the original student.txt file
            os.remove('student.txt')
                # Rename the tmp file
            os.rename('temp.txt', 'student.txt')
        else:
            # Remove the temp file
            os.remove('temp.txt')
    
            print('The information about the student id', delete_id,
                      'is not available in the data file.')
        
    
    
    except IOError:
        print('An unexpected error occurred during file reading or writing.')

    except Exception:
        print('An An unexpected error occurred during file renaming or deleting')      
    
    
    
    
    
    show_file('student.txt')
    
def show_file(file):
    file = open(file, 'r')
    sid = file.readline()
    print()
    print('-----------------------------------')
    print('ID   Last Name   First Name   Mark')
    print('-----------------------------------')
    
    while sid != '':
        
            sid = sid.rstrip()
            #print(sid)
            #read the line and  keep just the words       
            last_name = file.readline().rstrip()
            #print(last_name)
            
            first_name = file.readline().rstrip()
            #print(first_name)
          
            mark = float(file.readline().rstrip())
            #print(mark)
            
            print(f'{sid:5s}{last_name:12s}{first_name:13s}{mark}')
            
            sid = file.readline()
           
            #sid = sid.rstrip()  
    
    file.close()
    
main()
