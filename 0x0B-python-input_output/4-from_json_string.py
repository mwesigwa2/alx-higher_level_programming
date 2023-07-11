#!/usr/bin/python3
"""module to jsonify object"""


import json


def from_json_string(my_str):
    """function jsonifies objects"""
    return json.loads(my_str)
