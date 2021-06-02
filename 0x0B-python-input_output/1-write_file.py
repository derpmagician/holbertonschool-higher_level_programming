#!/usr/bin/python3
"""Function"""

def number_of_lines(filename=""):
    """ writes a string to a text file and returns the len of chars"""
    with open(filename, encoding='utf-8') as f:
        return len(f.readlines())
