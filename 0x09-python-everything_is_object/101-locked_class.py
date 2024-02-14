#!/usr/bin/python3
"""
a class LockedClass with no class or object attribute
"""


class LockedClass(object):
    """
    lass lockedclass  that prevent dinamically creating new instance
    Attributes except first_name
    """

    __slots__ = 'first_name'
