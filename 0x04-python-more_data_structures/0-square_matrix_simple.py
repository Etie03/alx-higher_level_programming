#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()

    for m in range(len(matrix)):
        new_matrix[m] = list(map(lambda x: x**2, matrix[m]))

    return (new_matrix)
