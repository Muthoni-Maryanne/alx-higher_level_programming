#!/usr/bin/python3
def islower(c):
    '''function that checks for lowercase character'''
    new = ord(c)
    if new >= 97 and new <= 122:
        print(f"{c} is lower")
    else:
        print(f"{c} is upper")
