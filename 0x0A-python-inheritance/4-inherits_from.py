#!/usr/bin/python3
"""Define inherits_from function"""


def inherits_from(obj, a_class):
    if isinstance(obj, a_class) and \
       issubclass(a_class, obj.__class__) is False:
        return True

    return False
