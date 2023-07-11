#!/usr/bin/python3
"""module that writes a string to a text file
   Return: number of characters written"""


def write_file(filename="", text=""):
    """writes a string to a text file"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
