#!/usr/bin/python3
"""Defines class Square"""


class Square:
    """class Square with one instance attribute and __init__ method"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes size and position attribute

        Args:
            size (int): The size of sides of the Square
            position (tuple): position of square

        Attributes:
            size (int): Private instance attribute
            position (tuple): Private instance attribute

        Raises:
            ValueError: if size is less than 0
            TypeError: if size is not an int
            TypeError: if position not tuple of 2 positive ints
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

        if type(position) is not tuple and len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.position = position

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

    @property
    def position(self):
        """tuple: Getter for the position attribute

        After is setter method which  modifies size with value::
            Args:
                value (tuple): new value of position

            Attributes:
                position (tuple): Private instance attribute

            Raises:
                TypeError: if position not tuple of 2 positive ints
        """
        if type(value) is not tuple and len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    @size.setter
    def position(self, value):
        if type(value) is not tuple and len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """Method that returns the current square area"""
        return (self.__size ** 2)

    def my_print(self):
        """ prints in stdout the square with the character #

        Note:
            if size is equal to 0, print an empty line
            position should be use by using space
            Don’t fill lines by spaces when position[1] > 0
        """
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
