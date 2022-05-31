# -*- coding: utf-8 -*-
"""
Created on Tue May 31 21:57:15 2022

@author: sebas
"""
"""
**Australian Population**
    
 The file 'auspopulation.txt' contains the Australian population from 1955
 onwards to 2015 at five year intervals
 ([source](https://www.worldometers.info/world-population/australia-population/)).
 Write a program that reads in the given data into a list. Calculate the average 
 five-yearly population *change* during the given period. Also display when the
 lowest five-year change was recorded.
    
 Download the file
 [auspopulation.txt](https://interact2.csu.edu.au/bbcswebdav/pid-4955210-dt-content-rid-18617593_1/xid-18617593_1)

"""


START_READ_YEAR = 1955


def main():
    
    pp_list = read_file('auspopulation.txt')
    
    pp_diff = []
    
    
    # Find population change by subtracting successive values
    for i in range(1,len(pp_list)):
        value = pp_list[i] - pp_list[i-1] 
        pp_diff.append(value)
    # Built in sequence functions can help
    average_change = sum(pp_diff)/len(pp_diff)
    print('Average change:', average_change)
    
    # Find minimum 5-yr change. Another built in function is applicable
    min_change = min(pp_diff)
    min_change_index = pp_diff.index(min(pp_diff))
    print('Minimum change recorded in', START_READ_YEAR  +  5 + (5 * min_change_index)," was " , min_change )
    
    print_list(pp_list)
    print_list(pp_diff)
    
    
def read_file(name):
    
    data_list =[]
    
    try:
    
        file = open(name,'r')
        for line in file:
            value = int(line)
            data_list.append(value)
        file.close()
        return data_list
    
                             
    except IOError:
        print('An unexpected error occurred during file I/O.')
        return -1
        
def print_list(list_g):
    
    
    print('------------------')
    print('Year   Population')
    print('------------------')
    year = START_READ_YEAR
    for i in range(0,len(list_g)):
        
        
        pp_year = list_g[i]
        print(f'{year:5d}{pp_year:12d}')           
        year+=5
    
    
    
    
    
    
main()














































