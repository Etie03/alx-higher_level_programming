#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []

    if len(matrix) > 0:
        for rows in matrix[:]:
            new_matrix.append(list(map(lambda x: x ** 2, rows)))

    return new_matrix
