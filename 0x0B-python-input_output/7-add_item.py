#!/usr/bin/python3
"""adds all arguments to a Python list"""
from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    js_list = load_from_json_file(filename)
except Exception as e:
    js_list = []
    with open(filename, 'w+') as f:
        pass

for arg in argv[1:]:
    json_list.append(arg)


save_to_json_file(ls, filename)
