#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[cln**2 for cln in row] for row in matrix]
    return new_matrix
