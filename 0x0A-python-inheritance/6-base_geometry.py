#!/usr/bin/python3
"""
The superclass of the geometries
"""


class BaseGeometry:
    """
    A super class that implements geometrical shapes
    """
    def area(self):
        raise Exception("area() is not implemented")
