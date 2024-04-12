#!/usr/bin/python3

def add_integer(a, b=98):
    ''' function that adds 2 integers'''
    try:
        if type(a) == int and type(b) == int:
            return (a + b)
        elif type(a) == float and type(b) == float:
            a = int(a)
            b = int(b)
            return (a + b)
        elif type(a) == float and type(b) == int:
            a = int(a)
            return (a + b)
        elif type(a) == int and type(b) == float:
            b = int(b)
            return (a + b)
        elif type(a) != int and type(a) != float:
            raise TypeError("a must be an integer")
        elif type(b) != int and type(b) != float:
            raise TypeError("b must be an int")

    except TypeError as t:
        return (t)
