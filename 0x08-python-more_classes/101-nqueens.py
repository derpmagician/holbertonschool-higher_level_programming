#!/usr/bin/python3
"""
N queens
"""


def nqueens(n, c=[]):
    """
    Args:
        n (int): size of board and number of queens.
        c (list): list of possible solutions
    """
    if rejected(n, c):
        return
    if accepted(n, c):
        print(c)
    s = first_candidate(n, c)
    while s is not None:
        n_queens(n, s)
        s = next_candidate(n, s)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        exit(1)
    n = sys.argv[1]
    if not n.isdigit():
        print('N must be a number')
        exit(1)
    n = int(n)
    if n < 4:
        print('N must be at least 4')
        exit(1)
    n_queens(n)
    exit(0)
© 2021 GitHub, Inc.
