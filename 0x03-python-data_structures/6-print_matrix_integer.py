#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for fila in matrix:
        for i in fila:
            print("{:d}".format(i), end=" " if fila[-1] != i else "")
    print()
