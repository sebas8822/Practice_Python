# -*- coding: utf-8 -*-
"""
Created on Thu May 26 11:24:15 2022

@author: sebas
"""

"""
Write a program to calculate the sum of the following series.
 The program should prompt the user for a positive integer n and display
 the sum of the series.
 
 s = 1+(1/2)+(1/4)+(1/8)...+1/2**n
 
"""
'''
n = int(input("Enter n")) 
s=0
for num in range(0,n):
    res = 2**num
    s = s+1/res  
    print(s,res)
'''

"""
Write a program that asks the user to enter the number of times that they 
have run around a racetrack, and then uses a loop to prompt them to enter
 the lap time for each of their laps. When the loop finishes, the program
 should display the time of their fastest lap, the time of their slowest 
 lap, and their average lap time.
"""

'''
lapTime = int(input("Enter lap Time -->"))

fastLap = lapTime
slowLap = lapTime
laps = 0
suma = 0


while (lapTime != -1):
    if (fastLap > lapTime):
       fastLap = lapTime
    else:
       slowLap = lapTime
    print("Faster Lap --> ",fastLap )  
    print("Lowest Lap --> ",slowLap )
    laps+=1
    suma = suma + lapTime   
    
    print("Lap --> ",laps  )
    print("Average --> ", suma/laps  )
      
       
    lapTime = int(input("Enter lap Time-->"))
    
'''    

"""
At a university, the tuition fee for a full-time student is $8,000 per
 semester. It has been announced that the fee will increase by 2 percent
 each year for the next 5 years. Write a program with a loop that displays
 the projected semester tuition amount for the next 5 years.
"""

'''

feeCurrentYear = 8000
feeIncrease = 0.02

incrementyear = 0

projectYear = int(input("Projected Years --> "))

for num in range(1,projectYear+1):
    incrementyear = (feeCurrentYear * feeIncrease)
    feeCurrentYear = feeCurrentYear + incrementyear # become
    
    
    print("Year ", num)
    print("Increment per year --> ", format(feeCurrentYear,'.2f'))

'''
"""
Write a program that should ask the user to enter a positive integer n. Based
 on the value of n, the program should use a nested loop to draw the following
 pattern with n rows:
     
*
**
***
****
*****

"""
'''
# double for

for i in range(1,10):# 1 to 9
   
    for j in range(i):
        print('*', end='  ')
    print()
'''


"""
 Write a program that uses nested loops to collect data and calculate 
 the average rainfall over a period of years. The program should first
 ask for the number of years. The outer loop will iterate once for each year.
 The inner loop will iterate twelve times, once for each month. Each iteration
 of the inner loop will ask the user for the millimetres of rainfall for 
 that month. After all iterations, the program should display the number
 of months, the total millimetres of rainfall, and the average rainfall 
 per month for the entire period.
"""
import random
num_years = random.randint(10,12)  # int(input("Insert number of years -->"))

print("Number of years: ",num_years )
for year in range(1,num_years+1):
    for month in range(1,12+1):
        rainfall_millimetres = random.randint(0,750)#int(input("Insert number of years -->"))
        print("Year:" + str(year) + " Month: "+ str(month)+ " Rain: " 
              + str(rainfall_millimetres) + "mm" )
    print()
    
        



