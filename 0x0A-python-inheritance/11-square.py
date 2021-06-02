#!/usr/bin/python3
"""
Define Square class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Initializes a square"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """return square area"""
        return self.__size ** 2

    def __str__(self):
        return '[Square] ' + str(self.__size) + '/' + str(self.__size)
