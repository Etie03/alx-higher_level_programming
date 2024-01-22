#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for m in range(len(matrix)):
        for p in range(len(matrix[m])):
            if p != 0:
                print(" ", end='')
            print("{:d}".format(matrix[m][p]), end='')
        print()
