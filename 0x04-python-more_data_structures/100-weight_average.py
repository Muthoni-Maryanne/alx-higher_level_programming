#!/usr/bin/python3
def weight_average(my_list=[]):
    '''returns the weighted average of

    all integers tuple (<score>, <weight>)'''
    if len(my_list) == 0 or my_list is None:
        return 0

    sum_ab = 0
    sum_b = 0
    for tuple_a in my_list:
        a, b = tuple_a
        sum_ab += (a * b)
        sum_b += b

    result = sum_ab/sum_b
    return result
