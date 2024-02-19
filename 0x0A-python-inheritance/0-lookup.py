#!/usr/bin/python3
"""returns the list of available attributes and methods of an object"""


def lookup(obj):
    """Gets the methods of the obj"""
    return dir(obj)
