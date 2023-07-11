#!/usr/bin/python3
"""module that adds attr to object"""


def add_attribute(obj, name, value):
    """adds attribute to obj"""
    if hasattr(obj, name):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
