#!/usr/bin/python3
""" Reads an utf-8 formated file line by line"""


def read_file(filename=""):
    with open(filename, encoding='utf-8') as f:
        for line in f:
            print(line, end='')
