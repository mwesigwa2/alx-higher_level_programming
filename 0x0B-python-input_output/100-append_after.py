#!/usr/bin/python3
"""module adds new string if certain srting is found """


def append_after(filename="", search_string="", new_string=""):
    """func adds new string if certain stringis found"""
    text = ""
    with open(filename) as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, 'w') as a_file:
        a_file.write(text)
