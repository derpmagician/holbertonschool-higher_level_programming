#!/usr/bin/python3
"""
Adds new atribute if possible
"""


def add_attribute(object, attribute, value):
    """adds a new attribute to an object if its possible"""
    if hasattr(object, "__dict__"):
        setattr(object, attribute, value)
    else:
        raise TypeError("can't add new attribute")
