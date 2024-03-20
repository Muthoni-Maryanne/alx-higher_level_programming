#!/usr/bin/python3
def uniq_add(my_list=[]):
    '''adds all unique integers in a list 

    (only once for each integer)'''
    total = 0
    for value in sorted(set(my_list)):
        if type(value) != int:
            break
        total += value
    return total
