# -*- coding: utf-8 -*-
"""
Created on Mon May 30 09:25:01 2022

@author: sebas
"""

import turtle


def main():
    try:
        points_file = open('q4_points.txt', 'r')

        line = points_file.readline()
        if line == '':
            print('Empty file')
            return

        x = int(line)

        line = points_file.readline()
        if line == '':
            print('Empty second line')
            return

        y = int(line)

        turtle.showturtle()
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()

        line = points_file.readline()
        while line != '':
            x = int(line)
            line = points_file.readline()
            if line == '':
                print('Empty line found, incomplete point data')
                return
            y = int(line)

            turtle.goto(x, y)

            line = points_file.readline()

        points_file.close()
        turtle.done()

    except ValueError:
        print('Invalid data found in file.')

    except IOError:
        print('An unexpected error occurred during file reading or writing.')


main()
