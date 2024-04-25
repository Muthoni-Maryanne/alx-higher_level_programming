#!/usr/bin/python3
"""Defines class MyList that inherits from list"""


class MyList(list):
    """Public instance method"""
    def print_sorted(self):
        """Creates copy of the list by accessing

        method in list class then sorts copy"""
        item = list.copy(self)
        print(sorted(item))
