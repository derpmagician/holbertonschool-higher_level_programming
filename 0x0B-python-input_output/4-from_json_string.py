#!/usr/bin/python3
"Method Module"
from json import loads


def from_json_string(my_str):
    """function that returns an object"""
    return loads(my_str)
