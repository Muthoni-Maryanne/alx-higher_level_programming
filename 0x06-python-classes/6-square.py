#!/usr/bin/python3
"""Defines class Square"""


class Square:
    """__init__ method to initialize attributes"""

    def __init__(self, size=0, position=(0, 0)):
        """private object size and position attribute"""
        self.__size = size
        if type(self.__size) is not int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
            
        self.__position = position
        if type(self.__position) is not tuple and len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @size.setter
    def position(self, value):
        if type(value) is not tuple and len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        if self.__size == 0:
            print("")
            return

        if position[1] < 0:
            for j in range(0, position[0]):
                print(" " * position[0])
            for i in range(0, self.__size):
                print("#" * self.__size)

        else:
            for i in range(0, self.__size):
                print("#" * self.__size)
