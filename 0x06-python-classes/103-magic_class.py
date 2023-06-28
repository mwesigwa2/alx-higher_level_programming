#!/usr/bin/python3
"""import the math module"""
import math


class MagicClass:
    """class that does the same as python bytecode"""
    def __init__(self, radius):
        if not isinstance(radius, (int, float)):
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        return math.pi * self.__radius ** 2

    def circumference(self):
        return 2 * math.pi * self.__radius
