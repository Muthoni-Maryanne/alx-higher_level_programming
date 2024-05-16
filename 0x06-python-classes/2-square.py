#!/usr/bin/python3
"""Defines class Square"""


class Square:
    """class Square with one instance attribute and __init__ method"""

    def __init__(self, size=0):
        """Initializes size attribute

        Args:
            size (int): The size of sides of the Square

        Attributes:
            size (int): Private instance attribute

        Raises:
            ValueError: if size is less than 0
            TypeError: if size is not an int
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
