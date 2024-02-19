#!/usr/bin/python3
"""Module for is_same_class method."""


def is_same_class(obj, a_class):
    """
     Checks if an object is exactly an instance of the specified class
    Args:
      - obj
      - a_class
    """
    return type(obj) == a_class
