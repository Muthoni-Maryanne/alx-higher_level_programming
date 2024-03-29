#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    '''adds 2 tuples'''
    if len(tuple_a) < 2:
        if len(tuple_a) == 0:
            tuple_a = 0, 0
        else:
            tuple_a = tuple_a[0], 0
    else:
        tuple_a = tuple_a[0:2]
    if len(tuple_b) < 2:
        if len(tuple_b) == 0:
            tuple_b = 0, 0
        else:
            tuple_b = tuple_b[0], 0
    else:
        tuple_b = tuple_b[0:2]

    result_tuple = tuple(x + y for x, y in zip(tuple_a, tuple_b))
    return result_tuple
