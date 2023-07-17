#!/usr/bin/python3
"""module of class rectangle that inherits from base"""
from models.base import Base


class Rectangle(Base):
    """class rectangle inherits from base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initializes Rectangle
        args:
            width: rectangle width
            height: rectangle height
            x: coordinate
            y: coordinate
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """returns the rectangle width"""
        return self.__width

    @width.setter
    def width(self, width):
        """initializes rectangle width"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        """returns the rectangle height"""
        return self.__height

    @height.setter
    def height(self, height):
        """initializes rectangle height"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        """returns x cordinate"""
        return self.__x

    @x.setter
    def x(self, x):
        """initializes x coordiante"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        """ returns y coordinate """
        return self.__y

    @y.setter
    def y(self, y):
        """initializes y cordinate"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """displays the rectangle using #"""
        print("\n" * self.__y, end="")
        for x in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """string representation of the rectangle"""
        return (f"[Rectangle] ({self.id}) "
                f"{self.__x}/{self.__y} - "
                f"{self.__width}/{self.__height}"
                )
