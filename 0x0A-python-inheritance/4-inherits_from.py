#!/usr/bin/python3
"""
Validate if a class inherits from a_class
"""


def inherits_from(obj, a_class):
    """Determines if an object is a true subclass of a class"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
