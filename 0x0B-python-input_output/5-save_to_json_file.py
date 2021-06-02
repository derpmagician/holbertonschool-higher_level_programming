#!/usr/bin/python3
"Method Module"
from json import dumps


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file"""
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(dumps(my_obj))
