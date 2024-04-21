#!/usr/bin/python3
"""class Rectangle that defines a rectangle"""


class Rectangle:
    """Defines class Rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes class Rectangle with args: self, width and height"""
        self.__width = width
        if not isinstance (self.__width, int):
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")
        
        self.__height = height
        if not isinstance (self.__height, int):
            raise TypeError("width must be an integer")
        if self.__height < 0:
            raise ValueError("width must be >= 0")

        type(self).number_of_instances += 1

    @property
    def width(self):
        """Retrieves value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Change value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Change value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return informal user-friendly string representation"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        list = []
        for i in range(self.__height):
            [list.append(Rectangle.print_symbol) for j in range(self.__width)]
            if i != self.__height - 1:
                list.append("\n")
        return ("".join(list))

    def __repr__(self):
        """Formal string representation interpreter can parse"""
        return "Rectangle(" + str(self.__width) + ", " + str(self.__height) + ")"

    def __del__(self):
        """Prints when an instance of Rectangle is deleted"""
        type(self).number_of_instances -= 
        print("Bye rectangle...")
