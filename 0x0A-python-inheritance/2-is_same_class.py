#!/usr/bin/python3
"""
Define is_same_class function
"""


def is_same_class(obj, a_class):
    """
    Checks if `obj` is exactly an instance of the specified class
    """

    if type(obj) == a_class:
        return True

    return False
