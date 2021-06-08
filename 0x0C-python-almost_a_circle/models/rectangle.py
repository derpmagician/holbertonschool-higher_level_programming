#!/usr/bin/python3
"""
The rectangle module with base as the superclass
"""
from models.base import Base


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
        """__width getter"""
        return self.__width

    @width.setter
    def width(self, v):
        """__width setter"""
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
            raise TypeError("height must be an integer")
        if v <= 0:
            raise ValueError("height must be > 0")
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
        """__width setter"""
        if type(v) is not int:
            raise TypeError("y must be an integer")
        if v < 0:
            raise ValueError("y must be >= 0")
        self.__y = v

    def area(self):
        """Calculates area of rectangle"""
        return self.width * self.height

    def display(self):
        """Displays rectangle using # character"""

        for row in range(self.y):
            print()
        for row in range(self.height):
            print('{}{}'.format(' ' * self.x, '#' * self.width))

    def __str__(self):
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(
                            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Updates multiple attributes"""
        argc = len(args)
        kwargc = len(kwargs)
        modif_attrs = ['id', 'width', 'height', 'x', 'y']

        if argc > 5:
            argc = 5

        if argc > 0:
            for i in range(argc):
                setattr(self, modif_attrs[i], args[i])
        elif kwargc > 0:
            for k, v in kwargs.items():
                if k in modif_attrs:
                    setattr(self, k, v)

    def to_dictionary(self):
        """Dictionary representation of a Rectangle"""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
