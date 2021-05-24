#!/usr/bin/python3
"""
A module with a Rectangle that does nothing
"""


class Rectangle:
    """
    An empty Rectangle class
    """

    def __init__(self, width=0, height=0):
        """
        Initializes some values
        Args:
            width (:obj:`int`, optional): The width of the Rectangle.
            height (:obj:`int`, optional): The height of the Rectangle.
        """

        self.__check_valid_width(width)
        self.__check_valid_height(height)

        self.width = width
        self.height = height

    @property
    def width(self):
        """getter of private instance width attribute"""
        self.__check_valid_width(width)

        return self._width

    @width.setter
    def width(self, value):
        """setter of private instance width attribute"""
        self._width = width

    @property
    def height(self):
        """getter of private instance height attribute"""
        self.__check_valid_height(height)

        return self._height

    @height.setter
    def height(self, value):
        """getter of private instance height attribute"""

    def __check_valid_width(self, width):
        """
        Checks if the width is a valid integer
        """
        if self.__check_int_value(width) is False:
            raise TypeError('width must be an integer')

        if self.__check_positive_value(width) is False:
            raise ValueError('width must be >= 0')

    def __check_valid_height(self, height):
        """
        Checks if the height is a valid integer
        """
        if self.__check_int_value(height) is False:
            raise TypeError('height must be an integer')

        if self.__check_positive_value(height) is False:
            raise ValueError('height must be >= 0')

    def __check_int_value(self, value):
        """
        Checks if the value is an integer
        """
        if type(value) is int:
            return True

        return False

    def __check_positive_value(self, value):
        """
        Checks if the value is a positive integer
        """
        if value >= 0:
            return True

        return False

    def area(self):
        """
        Returns:
            int: The area of a Rectangle.
        """

        return self.__width * self.__height

    def perimeter(self):
        """
        Returns:
            int: The perimeter of a Rectangle.
        """

        if self.__width == 0 or self.__height == 0:
            return 0

        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """
        Returns:
            str: 'Empty' If width or height is '0',
            or returns a string with the Rectangle.
        """
        rectstr = ''
        w = self.__width
        h = self.__height

        if w == 0 or h == 0:
            return rectstr

        for i in range(h):
            for j in range(w):
                rectstr += '#'

            if i != h - 1:
                rectstr += '\n'

        return rectstr

    def __repr__(self):
        """
        Returns the representation of the Rectangle.
        """
        w = str(eval('self.width'))
        h = str(eval('self.height'))

        return 'Rectangle(' + w + ', ' + h + ')'
