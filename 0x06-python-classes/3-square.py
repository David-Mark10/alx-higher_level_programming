#!/usr/bin/python3
"""Class Square definiation"""


class Square:
    """Stand for square

    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size=0):
        """Starts the square

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
