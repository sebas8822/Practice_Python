# -*- coding: utf-8 -*-
"""
Created on Tue May 31 23:16:55 2022

@author: sebas
"""

def main():
    # create A and B matrices with arbitrary data
    A = [ [3, -2, 5],
          [0, -1, 6],
          [-4, 2, -1] ]
    B = [ [2, -1, 0],
          [3, -5, 2],
          [1, 4, -2] ]

    C = matrix_multiply(A, B)

    print('C = A × B')
    print_matrix(C)

    # 3×3 identity matrix can be used for verifying multiply function
    I = [ [1, 0, 0], 
          [0, 1, 0],
          [0, 0, 1] ]
    D = matrix_multiply(B, I)  # result should be sae as B

    print('----------\nD = B × I = B')
    print_matrix(D)


def matrix_multiply(A, B):
    # Get n as the number of rows in A
    # Assume that all columns in A are of size n, similarly B is n×n
    # Validating the matrix sizes is laborious, so it is left out
    n = len(A)

    # Create empty zero-filled matrix C
    C = [[0 for i in range(n)] for j in range(n)]

    for row in range(n):
        for col in range(n):
            for tmp in range(n):
                C[row][col] += A[row][tmp] * B[tmp][col]

    return C


def print_matrix(M):
    """
    A function to print out an integer matrix with all columns aligned
    """
    n = len(M)
    for row in range(n):
        for col in range(n):
            print(format(M[row][col], '6d'), end='')  # for column alignment, width of 6 characters for each element
        print()


main()
