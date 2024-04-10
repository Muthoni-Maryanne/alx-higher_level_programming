#!/usr/bin/python3
def safe_print_division(a, b):
    '''divides 2 integers and prints the result'''
    try:
        result = a / b
    except (ZeroDivisionError, TypeError, ValueError):
        result = None
    except Exception as e:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return (result)
