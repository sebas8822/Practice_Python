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
        # Open original file for reading, and a temporary file for writing
        std_file = open('student.txt', 'r')
        tmp_file = open('tmp.txt', 'w')

        # Read the first student's id from the file
        delete_id = input('Enter the student id to be deleted: ')

        sid = std_file.readline()

        # Continue reading the file as long as we are not at the last line
        while sid != '':
            last_name = std_file.readline()
            first_name = std_file.readline()
            mark = std_file.readline()

            # Write all student information to tmp file, except for the deleted student
            if sid.rstrip() != delete_id:
                tmp_file.write(sid)  # All four variables already include a line break
                tmp_file.write(last_name)
                tmp_file.write(first_name)
                tmp_file.write(mark)
            else:
                deleted = True  # so that later we know to rename the tmp file
                print('The following information has been deleted from the student data file.')
                print(sid.rstrip() + '\t' + last_name.rstrip() + '\t' + first_name.rstrip() + '\t' + mark.rstrip())

            # Get id of the next student
            sid = std_file.readline()

        # Close the files
        std_file.close()
        tmp_file.close()

        if deleted:
            # Delete the original student.txt file
            os.remove('student.txt')
            # Rename the tmp file
            os.rename('tmp.txt', 'student.txt')

        else:
            # Remove the tmp file
            os.remove('tmp.txt')

            print('The information about the student id', delete_id,
                  'is not available in the data file.')

    except IOError:
        print('An unexpected error occurred during file reading or writing.')

    except Exception:
        print('An An unexpected error occurred during file renaming or deleting')


# Call the main function
main()
