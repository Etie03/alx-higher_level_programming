#!/usr/bin/python3
def square_matrix_simple(matrix):
    soln = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    for m in range(len(matrix)):
        for p in range(len(matrix[0])):
            soln[m][p] = matrix[m][p] ** 2

    return soln
