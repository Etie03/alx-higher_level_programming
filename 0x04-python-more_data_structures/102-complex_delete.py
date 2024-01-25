#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = []
    for m, p in a_dictionary.items():
        if p == value:
            keys.append(m)

    for m in keys:
        del a_dictionary[m]

    return a_dictionary
