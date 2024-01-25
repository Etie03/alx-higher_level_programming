#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    return sum([mul(m[0], m[1]) for m in my_list]) / sum(m[1] for m in my_list)


def mul(m, p):
    return m * p
