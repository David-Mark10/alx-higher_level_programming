#!/usr/bin/python3
"""Class type Square"""


class Square:
    """stand for a square

    Attributes:
        __size (int):the size of the side of square
    """
    def __init__(self, size=0):
        """initializes the square

        Args:
            size (int):The size of the side of square

        Returns:
            None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

    def area(self):
        return (self.__size) ** 2
