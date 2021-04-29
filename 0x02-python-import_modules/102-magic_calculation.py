#!/usr/bin/env python3
from magic_calculation_102 import add, sub


def magic_calculation(a, b, c):
    if a < b:
        return c
    if c > b:
        return a + b
    return a * b - c
