#!/usr/bin/python3
"""Module for read_file method"""


def read_file(filename=""):
    """Method for reading from file"""
    with open(filename, encoding='utf-8') as f:
        for line in f:
            print(line, end='')
