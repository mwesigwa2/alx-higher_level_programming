#!/usr/bin/python3
"""module with the class square that inherits from rectangle class"""
from models.ractangle import Rectangle


class Square(Rectangle):
    """class square that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string representation of a Square"""
        return (f"[Square] ({self.id}) "
                f"{self.x}/{self.y} - "
                f"{self.width}"
                )
