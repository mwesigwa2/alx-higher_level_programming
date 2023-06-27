#!/usr/bin/python3
"""class that defines a square with size validation"""


class Square:
    """define a private instance attribute"""


    def __init__(self, size=0):
        """initializes a square of length size"""
        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        if size < 0:
            raise ValueError("size must be >=0")
        self.__size = size
