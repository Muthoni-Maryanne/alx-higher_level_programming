#!/usr/bin/python3
def safe_print_integer(value):
    '''function that prints an integer with "{:d}".format()'''
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True
        else:
            raise ValueError
    except ValueError:
        return False
