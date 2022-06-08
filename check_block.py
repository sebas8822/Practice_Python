# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 15:07:30 2022

@author: sebas
"""


def check_block():
    block = ["A","B","C","D"]    
    ch = []
    input_block = str(input("enter shop number:  ")).upper()
    
    for i in input_block:
        ch.append(i)
       
        
        
    if len(ch)==4:
        try:
            block.index(ch[0])
            
            
            if (int(ch[1])>=1 and int(ch[1])<=6):
               if  int(ch[2])>=1 and int(ch[1])<=99:
                if  int(ch[3])>=1 and int(ch[3])<=99:
                    return True
        except :
            return False
            
      
    
            
def main():
    
    # print(check_block("b712"))# selected for number boundary
    # print(check_block("d1120"))# selected for # characters boundary
    # print(check_block("b11j"))# selected for incorrect input
    # print(check_block("j112"))# selectect boundary block
    # print(check_block("B112"))
    print(check_block())
    
main()