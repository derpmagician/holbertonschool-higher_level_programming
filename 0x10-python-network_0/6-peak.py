#!/usr/bin/python3
"""
finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    ''' Finds a peak in a list of unsorted integers. '''
    l = list_of_integers
    return max(l) if l else None
