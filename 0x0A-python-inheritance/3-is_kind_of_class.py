#!/usr/bin/python3
"""
This program validate the kind of class of an obj
"""


def is_kind_of_class(obj, a_class):
    '''Determines if an object is a subclass of a class.'''
    return isinstance(obj, a_class)
