#!/usr/bin/python3
"""Defines function that checks object is instance

of an inherited class"""


def inherits_from(obj, a_class):
    """
    Args:
        obj- The object to check.
        a_class-inherited class.
    Returns:
        True if obj is an inherited instance of a_class
        otherwise False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
