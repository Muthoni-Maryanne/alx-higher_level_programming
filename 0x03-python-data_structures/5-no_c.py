#!/usr/bin/python3
def no_c(my_string):
    '''removes all characters c and C from a string'''
    newstring = ''
    for letter in my_string:
        if letter == 'c':
            continue
        if letter == 'C':
            continue
        newstring += letter
    return newstring
