#!/usr/bin/python3
"""Checks if an object is exactly an instance of the specified class"""


def is_same_class(obj, a_class):
    """Determines if an object is exactly an instance of a class"""

     if type(obj) == a_class:
        return True

    return False
