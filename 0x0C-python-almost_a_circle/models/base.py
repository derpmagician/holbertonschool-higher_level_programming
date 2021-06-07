#!/usr/bin/python3
"""
The base module provides the Base class for the models module.
"""
import json
import csv
import turtle


class Base:
    """
    Uses private class attribute __nb_objects to manage the public instance
    attribute id in all our classes to avoid duplicated code or same bugs
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes id with input value or increment __nb_objects and assign
        its new value to id.
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
        """
        filename = cls.__name__ + ".json"
        if list_objs is not None:
            list_objs = [i.to_dictionary() for i in list_objs]
        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set
        **dictionary can be thought of as a double pointer to a dictionary
        """
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            dummy = cls(1, 1)
        elif cls is Square:
            dummy = cls(1)
        else:
            dummy = None
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances
        """
        from os import path
        filename = cls.__name__ + ".json"
        if not path.isfile(filename):
            return []
        with open(filename, "r", encoding="utf-8") as f:
            return [cls.create(**d) for d in cls.from_json_string(f.read())]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''Saves object to csv file.'''
        filename = cls.__name__ + ".csv"
        from models.rectangle import Rectangle
        from models.square import Square
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[o.id, o.width, o.height, o.x, o.y]
                             for o in list_objs]
            else:
                list_objs = [[o.id, o.size, o.x, o.y]
                             for o in list_objs]
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """
        Loads object to csv file.
        """
        filename = cls.__name__ + ".csv"
        from models.rectangle import Rectangle
        from models.square import Square
        new = []
        with open(filename, "r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                row = [int(r) for r in row]
                if cls is Rectangle:
                    d = {"id": row[0], "width": row[1], "height": row[2],
                         "x": row[3], "y": row[4]}
                else:
                    d = {"id": row[0], "size": row[1],
                         "x": row[2], "y": row[3]}
                new.append(cls.create(**d))
        return new

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draw
        """
        
        from random import randint
        lists = list_rectangles + list_squares
        turtle.colormode(255)
        turtle.bgcolor("#1c1c1c")
        t = turtle.Turtle()
        t.shape("turtle")
        t.color("#ffffff")
        j = -200
        y = -200
        t.pensize(5)
        for i in lists:
            t.color((randint(1, 255), randint(1, 255), randint(1, 255)))
            t.penup()
            t.goto(j, y)
            j += 50
            y += 50
            t.pendown()
            for r in range(2):
                t.begin_fill()
                t.back(i.width)
                t.left(90)
                t.back(i.height)
                t.left(90)
                t.end_fill()
            t.left(-30)

        turtle.exitonclick()
