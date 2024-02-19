#!/usr/bin/python3
"""
Validate if a class inherits from a_class
"""


def inherits_from(obj, a_class):
    if isinstance(obj, a_class) and \
       issubclass(a_class, obj.__class__) is False:
        return True

    return False
