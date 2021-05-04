#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    copy_a = (tuple_a + (0, 0))[:2]
    copy_b = (tuple_b + (0, 0))[:2]
    return tuple(map(sum, zip(copy_a, copy_b)))
