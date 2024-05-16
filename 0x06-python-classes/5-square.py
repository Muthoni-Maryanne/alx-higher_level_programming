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

    @property
    def size(self):
        """int: Getter for the size attribute, returns int

        After is setter method which  modifies size with value::
            Args:
                value (int): new value of size

            Attributes:
                size (int): size of side of Square

            Raises:
                ValueError: if size is less than 0
                TypeError: if size is not an int
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Method that returns the current square area"""
        return (self.__size ** 2)

    def my_print(self):
        """ prints in stdout the square with the character #

        Note:
            if size is equal to 0, print an empty line
        """
        for i in range(0, self.__size):
            print('#' * self.__size)
        if self.__size == 0:
            print('')
