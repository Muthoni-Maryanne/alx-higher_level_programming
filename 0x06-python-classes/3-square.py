#!/usr/bin/python3
"""Defines class Square"""


class Square:
    """__init__ method to initialize attributes"""

    def __init__(self, size=0):
        """private object size attribute"""
        self.__size = size

        if type(self.__size) is not int:
            raise TypeError("size must be an integer")

        if self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return (self.__size ** 2)
