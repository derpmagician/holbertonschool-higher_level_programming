#!/usr/bin/python3
"""adds all arguments to a Python list"""


from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    ls = load_from_json_file(filename)
except:
    ls = []

ls += [arg for arg in argv[1:]]
save_to_json_file(ls, filename)
