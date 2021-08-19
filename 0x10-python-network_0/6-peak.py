#!/usr/bin/python3
"""
finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """ Finds a peak in a list of unsorted integers. """

    my_list = list_of_integers
    l = 0
    r = len(my_list) - 1

    if not my_list:
        return None

    while (l < r):
        center = (l + r) // 2
        if my_list[center] < my_list[center + 1]:
            l = center + 1
        else:
            r = center

    return my_list[l]


