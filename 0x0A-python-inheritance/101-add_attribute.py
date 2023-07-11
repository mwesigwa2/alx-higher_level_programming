#!/usr/bin/python3
"""module that adds attr to object"""


def add_attribute(obj, attr, value):
    """adds attribute to obj"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")

    obj.__dict__[attr] = value
