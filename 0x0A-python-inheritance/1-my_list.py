#!/usr/bin/python3
"""class MyList that inherits from list"""


class MyList(list):
    '''Custom MyList class.'''
    def print_sorted(self):
        '''Method for printing sorted list.'''
        print(sorted(self))
