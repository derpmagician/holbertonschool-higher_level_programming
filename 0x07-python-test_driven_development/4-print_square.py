#!/usr/bin/python3
"""
This module prints a square with the # char
of any positive integer size.
Example:
    ###
    ###
    ###
"""


def print_square(size):
    """
    Prints the #
    Args:
        size (int): The size of the square to prints.
    Raises:
        TypeError: If `size` isn't int.
        ValueError: If `size` < 0.
    """

    if type(size) is not int:
        raise TypeError('size must be an integer')

    if size < 0:
        raise ValueError('size must be >= 0')

    for i in range(1, size**2 + 1):
        print('#', end='')
        if i % size == 0 and i > 0:
            print()
