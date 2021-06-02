#!/usr/bin/python3
"Method Module"
from os import path
from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    json_list = from_json_file(filename)
except Exception as e:
    json_list = []
    with open(filename, 'w+') as f:
        pass

for arg in argv[1:]:
    json_list.append(arg)

to_json_file(json_list, filename)
