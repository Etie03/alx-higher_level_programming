#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for m in my_string:
        if m != 'c' and m != 'C':
            new_string += m
    return new_string
