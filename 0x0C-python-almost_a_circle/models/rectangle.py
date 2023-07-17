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
