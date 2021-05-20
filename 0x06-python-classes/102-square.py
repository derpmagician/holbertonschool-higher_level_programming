#!/usr/bin/python3
"""
A Square Class
"""


class Square:
    """ represents a square """
    def __init__(self, size=0):
        """Size is a private attribute"""
        self.size = size

    def __gt__(self, other):
        """ > """
        return self.area() > other.area()

    def __ge__(self, other):
        """ >= """
        return self.area() >= other.area()

    def __le__(self, other):
        """ <= """
        return self.area() <= other.area()

    def __lt__(self, other):
        """ <  """
        return self.area() < other.area()

    def __eq__(self, other):
        """ Method == """
        return self.area() == other.area()

    def __ne__(self, other):
        """ Method != """
        return self.area() != other.area()

    @property
    def size(self):
        """Property of size"""
        return self.__size

    @size.setter
    def size(self, new_size):
        """setter of size"""
        if not isinstance(new_size, int):
            raise TypeError("size must be an integer")
        elif new_size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = new_size

    def area(self):
        """Public instance method:
           * Return: the current square area"""
        return(self.__size * self.__size)
