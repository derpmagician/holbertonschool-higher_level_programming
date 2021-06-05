#!/usr/bin/python3
"""
The base module provides the Base class for the models module.
"""
import json


class Base:
    """
    Uses private class attribute __nb_objects to manage the public instance
    attribute id in all our future classes to avoid duplicated code
    (by extension, same bugs).
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes id with input value or increment __nb_objects and assign
        its new value to `id`.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or not len(list_dictionaries):
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns a list of the JSON string representation json_string
        """
        if not isinstance(json_string, str) or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file
        The filename must be: <Class name>.json - example: Rectangle.json
        You must use the static method to_json_string
        """
        filename = cls.__name__ + ".json"
        if list_objs is not None:
            list_objs = [i.to_dictionary() for i in list_objs]
        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))
