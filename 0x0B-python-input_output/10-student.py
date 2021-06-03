#!/usr/bin/python3
"""Student Class"""


class Student:
    """Initilization"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        class_d = self.__dict__
        sel_d = dict()

    def to_json(self, attrs=None):
        """Returns a dictionary"""
        if attrs is None:
            return self.__dict__
        my_dict = dict()
        for attr in attrs:
            if attr in self.__dict__:
                my_dict[attr] = self.__dict__[attr]
        return my_dict
