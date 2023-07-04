#!/usr/bin/python3
"""definition of a rectangle"""


class Rectangle:
    """definition of a rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ sets width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get width"""
        return self.__height

    @height.setter
    def height(self, value):
        """ sets height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """gets area of rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """gets perimeter of rectangle"""
        if (self.__height == 0 or self.__width == 0):
            return 0
        return (2 * (self.__height + self.__width))

    def __str__(self):
        """returns string representation of rectangle"""
        if (self.__height == 0 or self.__width == 0):
            return ("")
        return ("\n".join([str(self.print_symbol)
                           * self.__width] * self.__height))

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
