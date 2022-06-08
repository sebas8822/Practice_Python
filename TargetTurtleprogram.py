# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 20:20:31 2022

@author: sebas
"""

import turtle
import random
import time

turtle.reset() #Rest Program
turtle.speed(0)#Setup Speed 0 for faster
# Named constants global scope
ScreenSize = 500    # Screen width it is a square
turtle.setup(ScreenSize, ScreenSize)
ws = turtle.Screen()

def main():
    
    draw_square()
    
    for i in range (10):
        ramdom_position()
        turtle.stamp()
        determine()
        time.sleep(1)

def draw_square():
        
    
    turtle.showturtle()
    
    
    turtle.penup()
    turtle.goto(-300, -300)
    turtle.pendown()
  
    turtle.goto(450, -300)
    
    turtle.goto(450, 200)
    turtle.goto(-300, 200)
    turtle.goto(-300, -300)
    turtle.penup()
    
def ramdom_position():
    turtle.goto(random.randint(-500, 500),random.randint(-500, 500))
    print(turtle.xcor())
    
def determine():
    
    if(turtle.xcor() >=-300 and turtle.xcor() <=450 and turtle.ycor()>=-300 and turtle.ycor()<=200 ):
        turtle.write(str(turtle.pos()) + str(turtle.xcor()) + " target hit!", align='center', font=('Verdana', 10, 'bold'))
        print('Target hit!')
        target_hit()
    else:
        turtle.write(str(turtle.pos()) + str(turtle.xcor()) + " miss hit!", align='center', font=('Verdana', 10, 'bold'))        
        print('miss hit!')
        miss_target()
        
        
def target_hit():
    
    turtle.fillcolor('pale green')
    turtle.begin_fill()
    for j in range(4):
        turtle.forward(50)
        turtle.left(90)
    turtle.end_fill()
    
def miss_target():
    
    turtle.pensize(10) 
    turtle.pencolor("Blue")
    turtle.pendown()
    turtle.circle(75)
    turtle.penup()
    
    

    
    
    
    
main()
turtle.done()