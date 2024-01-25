#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    b_dictionary = a_dictionary.copy()

    for m, p in b_dictionary.items():
        b_dictionary[m] = p * 2

    return b_dictionary
