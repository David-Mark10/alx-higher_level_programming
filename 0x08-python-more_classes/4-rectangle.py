#!/usr/bin/python3
"""
Rectangle module that does nothing
"""


class Rectangle:
    """
    An empty Rectangle class
    """

    def __init__(self, width=0, height=0):
        """
        To check parameters and initializes values
        Args:
            width (:obj:`int`, optional): The width of the Rectangle.
            height (:obj:`int`, optional): The height of the Rectangle.
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Returns the width of the Rectangle
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        To check parameters and set size of the Rectangle
        Args:
            value (int): The width of the Rectangle.
        Raises:
            TypeError: If `value` type is not `int`.
            ValueError: If `value` is less than `0`.
        """

        self.__check_valid_width(value)
        self.__width = value

    @property
    def height(self):
        """
        Returns the width of the Rectangle
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        To check parameters and set size of Rectangle
        Args:
            value (int): The height of the Rectangle.
        Raises:
            TypeError: If `value` type is not `int`.
            ValueError: If `value` is less than `0`.
        """

        self.__check_valid_height(value)
        self.__height = value

    def __check_valid_width(self, width):
        """
        To check if width is valid integer
        Args:
            width (int): The width of the Rectangle.
        Raises:
            TypeError: If `width` type is not `int`.
            ValueError: If `width` is less than `0`.
        """

        if self.__check_int_value(width) is False:
            raise TypeError('width must be an integer')

        if self.__check_positive_value(width) is False:
            raise ValueError('width must be >= 0')

    def __check_valid_height(self, height):
        """
        To check if height is valid integer
        Args:
            height (int): The height of the Rectangle.
        Raises:
            TypeError: If `height` type is not `int`.
            ValueError: If `height` is less than `0`.
        """

        if self.__check_int_value(height) is False:
            raise TypeError('height must be an integer')

        if self.__check_positive_value(height) is False:
            raise ValueError('height must be >= 0')

    def __check_int_value(self, value):
        """
        To check if value is integer
        Args:
            value (int): The number to verify
        Returns:
            int: If is a int `True`, `False` otherwise.
        """

        if type(value) is int:
            return True

        return False

    def __check_positive_value(self, value):
        """
        To check if value is positive integer
        Args:
            value (int): The number to verify
        Returns:
            int: `True` If value is greater than
            or equal to 0, `False` otherwise.
        """

        if value >= 0:
            return True

        return False

    def area(self):
        """
        Computes area of the Rectangle.
        Returns:
            int: Rectangle area.
        """

        return self.__width * self.__height

    def perimeter(self):
        """
        Compute perimeter of Rectangle.
        Returns:
            int: perimeter of Rectangle.
        """

        if self.__width == 0 or self.__height == 0:
            return 0

        return self.__width * 2 + self.__height * 2

    def __draw_rectangle(self):
        """
        Draw Rectangle with size
        Returns:
            str: `Empty` If width or height is `0`,
            otherwise returns a string with the Rectangle.
        """

        rect_str = ''
        w = self.__width
        h = self.__height

        if w == 0 or h == 0:
            return rect_str

        for i in range(h):
            for j in range(w):
                rect_str += '#'

            if i != h - 1:
                rect_str += '\n'

        return rect_str

    def __str__(self):# Return string with representation of the Rectangle.

        return self.__draw_rectangle()

    def __repr__(self):# Return representation of the Rectangle.
        w = str(eval('self.width'))
        h = str(eval('self.height'))

        return 'Rectangle(' + w + ', ' + h + ')'
