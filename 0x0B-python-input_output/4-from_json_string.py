#!/usr/bin/python3
"""module to jsonify object"""


import json


def from_json_string(my_obj):
    """function jsonifies objects"""
    return json.dumps(my_obj)
