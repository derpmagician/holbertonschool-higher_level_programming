#!/usr/bin/python3
"""
Define class BaseGeometry
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ Square class that inherits from Rectangle """
    def __init__(self, size):
        """ Initializes validated private instance __width """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """" Returns the area of the square """
        return self.__size ** 2
