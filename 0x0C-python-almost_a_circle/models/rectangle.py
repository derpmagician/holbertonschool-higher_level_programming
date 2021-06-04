#!/usr/bin/python3
"""
The rectangle module with base as the superclass
"""
from base import Base


class Rectangle(Base):
    """
    A Rectangle class using private instance attributes with individual
    getters and setters.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes id using Base class __init__
        Initializes __width, __height, __x, and __y
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """__width` getter"""
        return self.__width

    @width.setter
    def width(self, v):
        """__width` setter"""
        if type(v) is not int:
            raise TypeError("width must be an integer")
        if v <= 0:
            raise ValueError("width must be > 0")
        self.__width = v

    @property
    def height(self):
        """__height getter"""
        return self.__height

    @height.setter
    def height(self, v):
        """__height setter"""
        if type(v) is not int:
            raise TypeError("width must be an integer")
        if v <= 0:
            raise ValueError("width must be > 0")
        self.__height = v

    @property
    def x(self):
        """__x getter"""
        return self.__x

    @x.setter
    def x(self, v):
        """__x setter"""
        if type(v) is not int:
            raise TypeError("x must be an integer")
        if v < 0:
            raise ValueError("x must be >= 0")
        self.__x = v

    @property
    def y(self):
        """__y getter"""
        return self.__y

    @y.setter
    def y(self, v):
        """__width` setter"""
        if type(v) is not int:
            raise TypeError("y must be an integer")
        if v < 0:
            raise ValueError("y must be >= 0")
        self.__y = v
