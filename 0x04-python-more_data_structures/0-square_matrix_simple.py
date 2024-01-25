#!/usr/bin/python3
def square_matrix_simple(matrix):
      new_matrix = [x[:] for x in matrix]
      for m in range(len(new_matrix)):
          for p in range(len(new_matrix[m])):
              new_matrix[m][p] = (new_matrix[m][p]) ** 2


      return new_matrix
