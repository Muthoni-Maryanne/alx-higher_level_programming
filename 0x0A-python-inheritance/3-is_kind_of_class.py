#!/usr/bin/python3
"""Defines a function that checks if

an object is an instance or inherited instance of a class."""


def is_kind_of_class(obj, a_class):
    """
    args:
        obj- the object/instance
        a_class- the class

    Return:
        True if object is an instance or inherited
        instance of a class, otherwise False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
