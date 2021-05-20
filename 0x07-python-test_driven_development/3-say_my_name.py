#!/usr/bin/python3
"""
This module prints the names
Output: 'My name is <first name> <last name>'
"""


def say_my_name(first_name, last_name=""):
    """
    Prints the names
    Args:
        first_name (str): The first name.
        last_name (str): The last name.
    Raises:
        TypeError: If `first_name` and `last_name` aren't strings.
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is", first_name, last_name)
