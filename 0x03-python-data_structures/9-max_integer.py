#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None

    max_val = min(my_list)
    for m in my_list:
        if m > max_val:
            max_val = m

    return max_val
