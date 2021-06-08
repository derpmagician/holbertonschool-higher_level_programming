#!/usr/bin/python3
"""
The squares module contains Rectangle as the superclass
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A representation of a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializes the square"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for size"""
        self.width = value
        self.height = value

    def __str__(self):
        """informal string representation of the square"""
        string = "[Square] ({:d}) {:d}/{:d} - {:d}"
        string = string.format(self.id, self.x, self.y, self.width)
        return string

    def update(self, *args, **kwargs):
        """update attributes"""
        args_list = ["id", "width", "x", "y"]
        if args and args[0] is not None:
            if len(args) > len(args_list):
                max_len = len(args_list)
            else:
                max_len = len(args)
            for i in range(max_len):
                setattr(self, args_list[i], args[i])
        elif kwargs is not None:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """dictionary representation of a Square"""
        key_list = ["id", "size", "x", "y"]
        value_list = [self.id, self.width, self.x, self.y]
        return dict(zip(key_list, value_list))
