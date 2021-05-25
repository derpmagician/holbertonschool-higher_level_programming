#!/usr/bin/python3
"""
N queens
"""


def check_if_number():
    """
    check if n is a number
    """
    for i in sys.argv[1]:
        if i < '0' or i > '9':
            print("N must be a number")
            exit(1)

def check_if_4_big():
    """
    check if is 4 or more
    """
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        exit(1)

def check_valid_n():
    """
    Checks if is a valid number
    """

    check_if_number()
    check_if_4_big()


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    check_valid_n()


