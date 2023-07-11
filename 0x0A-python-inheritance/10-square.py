#!/usr/bin/python3
"""module with class inheriting from rectangle"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """child to square"""
    def __init__(self, size):
        """initiates square"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return (self.__size * self.__size)
