#!/usr/bin/python3
"""
A function "4-print_square" module.
A function that prints the square with #
"""


def print_square(size):

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        print(("#" * size + "\n") * size, end="")
