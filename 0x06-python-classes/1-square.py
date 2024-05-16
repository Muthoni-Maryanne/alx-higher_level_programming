#!/usr/bin/python3
"""Defines class Square"""


class Square:
    """class Square with one instance attribute and __init__ method"""

    def __init__(self, size):
        """Initializes size attribute

        Args:
            size (int): The size of sides of the Square

        Attributes:
            size (int): Private instance attribute
        """
        self.__size = size
