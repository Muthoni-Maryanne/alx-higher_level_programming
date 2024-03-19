#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    '''prints a matrix of integers'''
    for row in matrix:
        for i in range(len(row)):
            print("{:d}".format(row[i]), end=' ')
        print()
