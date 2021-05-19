#!/usr/bin/python3
"""MagiClass"""


class MagicClass:
    """"Class for Area of a circle"""
    def __init__(self, radius=0):
        """Initialization

        Args:
            radius (int/float): attribute"""
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """Area: area"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Circumference: circumference"""
        return 2 * math.pi * self.__radius
