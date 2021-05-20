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

    for i in range(1, size + 1):
        for j in range(1, size + 1):
            print('#', end='')

            if j % size == 0 and j > 0:
                print()
