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

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(self.__size) is not int:
            raise TypeError("size must be an integer")

        if self.__size < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        for i in range(0, self.__size):
            print('#' * self.__size)
        if self.__size == 0:
            print('')
