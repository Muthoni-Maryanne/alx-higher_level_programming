#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    '''prints all integers of a list, in reverse order'''
    idx = -1
    while idx >= (-1 * len(my_list)):
        number = my_list[idx]
        print("{:d}".format(number))
        idx -= 1
