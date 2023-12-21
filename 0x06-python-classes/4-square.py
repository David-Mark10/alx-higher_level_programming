#!/usr/bin/python3
"""Class Square Defination"""


class Square:
    """Represents a square

    Attributes:
        __size (int): size of the side of square
    """
    def __init__(self, size=0):
        """initializes the square

        Args:
            size (int): size of the side of square

        Returns:
            None
        """
        self.size = size

    def area(self):
        """calculates area of square's

        Returns:
            The area of the square
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """getter of __size

        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
