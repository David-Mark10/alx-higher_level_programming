#!/usr/bin/python3
"""Class square definition"""


class Square:
    """ Class type square

    Attributes:
        __size (int):The size of the side square
    """
    def __init__(self, size):
        """This is to Initializes a square

        Args:
            size (int): The square size of the side

        Returns: None
        """
        self.__size = size
