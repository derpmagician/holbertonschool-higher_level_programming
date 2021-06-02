#!/usr/bin/python3
"""
Define class BaseGeometry
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class initlization
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size 

    def area(self):
        """"Returns the area of the square"""
        return self.__size ** 2
