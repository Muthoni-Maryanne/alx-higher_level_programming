#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    '''finds all multiples of 2 in a list'''
    list = []
    for number in my_list:
        if number % 2 == 0:
            list.append(True)
        else:
            list.append(False)
    return list
