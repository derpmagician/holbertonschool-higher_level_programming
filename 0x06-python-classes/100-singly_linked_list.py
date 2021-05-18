#!/usr/bin/python3
"""
A group of classes
"""


class Node:
    """ Node class """
    def __init__(self, data, next_node=None):
        """ Initializes private instance
            positive integer `__data` and `__next_node` """
        if type(data) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = data

        if type(next_node) is not Node and \
           next_node is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = next_node

    @property
    def data(self):
        """ getter for `__data` """
        return self.__data

    @data.setter
    def data(self, value):
        """ setter for `__data` """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """ getter for `__next_node` """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ setter for `__next_node` """
        if type(value) is not Node and \
           value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value

class SinglyLinkedList:
    """ Singly linked list class """
    def __init__(self):
        """ initialize private instance Node `__head` """
        self.__head = None

    def sorted_insert(self, value):
        """ insert new node into singly linked list """
        new = Node(value, self.__head)
        prev = None
