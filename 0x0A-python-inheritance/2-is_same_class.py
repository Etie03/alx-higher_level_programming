#!/usr/bin/python4
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """
    This function validate if obj is the same class of a_clas
    Args:
      - obj
      - a_class
    """
    return type(obj) == a_class
