#!/usr/bin/python3
""" Reads an utf-8 formated file line by line"""


def read_file(filename=""):
    """Reads an UTF8 formated file line by line """
    with open(filename, encoding='utf-8') as f:
        for line in f:
            print(line, end='')
