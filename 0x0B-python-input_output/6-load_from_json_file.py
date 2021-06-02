#!/usr/bin/python3
"Method Module"
from json import loads


def load_from_json_file(filename):
    """function that loads an Object"""
    with open(filename, encoding='utf-8') as f:
        return loads(f.read())
