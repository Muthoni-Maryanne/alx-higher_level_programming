#!/usr/bin/python3
"""Defines function that checks if object is

instance of a specified class or not"""


def is_same_class(obj, a_class):
    """Returns True or False"""
    if type(obj) is a_class:
        return True
    else:
        return False
