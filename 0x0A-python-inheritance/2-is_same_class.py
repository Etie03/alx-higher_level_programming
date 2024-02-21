#!/usr/bin/python3
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """
    Determines if an object is exactly an instance of a class
    """
    return type(obj) is a_class
