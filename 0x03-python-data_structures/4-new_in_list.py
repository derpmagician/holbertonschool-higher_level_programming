#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_copy = my_list.copy()
    if 0 <= idx < len(my_list):
        my_copy[idx] = element
    return my_copy
