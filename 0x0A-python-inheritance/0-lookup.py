#!/usr/bin/python3
"""Defines an object attribute and methods lookup function."""


def lookup(obj):
    """function that returns the list of

    available attributes and methods of an object"""
    a = dir(obj)
    return (a)
