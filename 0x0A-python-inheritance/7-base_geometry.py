#!/usr/bin/python3
class BaseGeometry:
    """
    A super class that implements geometrical shapes
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Checks a integer value
        Raises:
            TypeError: If `value` isn't a integer.
            ValueError: If `value` is less than or equal to zero.
        """

        if type(value) is not int:
            raise TypeError(name + ' must be an integer')

        if value <= 0:
            raise ValueError(name + ' must be greater than 0')
