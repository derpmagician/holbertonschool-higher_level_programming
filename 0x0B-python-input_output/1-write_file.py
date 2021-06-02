#!/usr/bin/python3
"""Function to write text"""


def write_file(filename="", text=""):
    """function that writes a string to a text file"""
    with open(filename, 'w', encoding="utf-8") as f:
        return(f.write(text))
