#!/usr/bin/python3
"""write object to json file"""


import json


def save_to_json_file(my_obj, filename):
    """write object to json text file"""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
