# -*- coding: utf-8 -*-
"""
Created on Sat May 28 12:13:01 2022

@author: sebas
"""

"""
Write a program that reads the student data file ‘students.txt’ 
(containing the same record structure as exercise 1) and displays the records 
of only the students having marks more than 80. Your program should handle
 all file I/O exceptions.
 """
def main():
    #try:
        # Open a file for writing
        std_file = open('student.txt', 'r')

        # Read the first student's id from the file
        sid = std_file.readline()
        print('List of excellent student(s):')
        print('ID   Last Name   First Name   Mark')
        print('-----------------------------------')
        
        print(std_file.readline().rstrip())
"""
        while sid != '':

            last_name = std_file.readline().rstrip()
            first_name = std_file.readline().rstrip()
            try:
                mark = float(std_file.readline().rstrip())
            except ValueError:
                print('Invalid mark data found in file.')
            else:
                # Display the student records having marks more than 80
                if 80 < mark <= 100:
                    sid = sid.rstrip()
                    # Use Python f-strings for easier column alignment. We don't have to use them but f-strings make it
                    # easy to format complex strings. See this link for an introduction: https://bit.ly/2ON71o7
                    print(f'{sid:5s}{last_name:12s}{first_name:13s}{mark}')

            # Get id of the next student
            sid = std_file.readline()

        # Close the file
        std_file.close()

    except IOError:
        print('An unexpected error occurred during file I/O.')
"""

# Call the main function
main()