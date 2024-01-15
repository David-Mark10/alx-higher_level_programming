#!/usr/bin/python3
"""
A function def pascal_triangle(n): that returns a list of
lists of integers representing the Pascals triangle of n:
"""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.

    Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        trgl = triangles[-1]
        tmp = [1]
        for j in range(len(trgl) - 1):
            tmp.append(trgl[j] + trgl[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
