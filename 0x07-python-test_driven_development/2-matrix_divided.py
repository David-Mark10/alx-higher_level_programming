#!/usr/bin/python3
"""
A function 2-matrix_divided that divide all matrix.
and accept two argument
"""


def matrix_divided(matrix, div):
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    size = None
    for j in matrix:
        if type(j) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if size is None:
            size = len(j)
        elif size != len(j):
            raise TypeError("Each row of the matrix must have the same size")
        for k in j:
            if type(k) is not int and type(k) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(k / div, 2) for k in j] for j in matrix]
