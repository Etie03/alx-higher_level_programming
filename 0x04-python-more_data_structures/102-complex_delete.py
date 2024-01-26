#!/usr/bin/python3
def complex_delete(my_dict, value):
    tmp = my_dict.copy()
    for m, p in tmp.items():
        if value == p:
            my_dict.pop(m)
            return my_dict
