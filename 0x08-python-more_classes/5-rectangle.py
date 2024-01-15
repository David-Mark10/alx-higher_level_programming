#!/usr/bin/python3

class Rectangle:
    """
    An empty Rectangle class
    """

    def __init__(self, width=0, height=0):#To check parameters and initialize the values
        """Args:
            width (:obj:`int`, optional): The Rectangle width.
            height (:obj:`int`, optional): The rectangle height.
        """

        self.width = width
        self.height = height

    def __del__(self):
        """
        Prints details when an instance Rectangle is deleted
        """

        print('Bye rectangle...')

    @property
    def width(self):
        """
        Returns rectangle width
        """

        return self.__width

    @width.setter
    def width(self, value):#To check parameters and set rectangle size
        """Args:
            value (int): The rectangle width.
        Raises:
            TypeError: If `value` type is not `int`.
            ValueError: If `value` is less than `0`.
        """

        self.__check_valid_width(value)
        self.__width = value

    @property
    def height(self):
        """
        Returns Rectangle width
        """

        return self.__height

    @height.setter
    def height(self, value):# To check parameters and set size of Rectangle
        """Args:
            value (int):Rectangle height.
        Raises:
            TypeError: If `value` type is not `int`.
            ValueError: If `value` is less than `0`.
        """

        self.__check_valid_height(value)
        self.__height = value

    def __check_valid_width(self, width):#To checks if width is valid integer
        """Args:
            width (int): Rectangle width.
        Raises:
            TypeError: If `width` type is not `int`.
            ValueError: If `width` is less than `0`.
        """

        if self.__check_int_value(width) is False:
            raise TypeError('width must be an integer')

        if self.__check_positive_value(width) is False:
            raise ValueError('width must be >= 0')

    def __check_valid_height(self, height):#To checks if height is valid integer
        """Args:
            height (int): Rectangle height.
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
        Check if value is integer
        Args:
            value (int):Number to verify
        Returns:
            int: If int `True`, otherwise `False`.
        """

        if type(value) is int:
            return True

        return False

    def __check_positive_value(self, value):
        """
        Check if value is positive integer
        Args:
            value (int): Number to verify
        Return:
            int: `True` If value is equal to or greater than
            0, `False` otherwise.
        """

        if value >= 0:
            return True

        return False

    def area(self):
        """
        Compute area of Rectangle.
        Returns:
            int: Area of Rectangle.
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
        Draw a Rectangle with their size
        Return:
            str: `is empty` If hight or width is `0`,
            otherwise return a string with the Rectangle.
        """

        rect_str = ''
        wth = self.__width
        hght = self.__height

        if wth == 0 or hght == 0:
            return rect_str

        for a in range(hght):
            for i in range(wth):
                rect_str += '#'

            if a != hght - 1:
                rect_str += '\n'

        return rect_str

    def __str__(self):
        """
        Return a string with representation of the Rectangle.
        """

        return self.__draw_rectangle()

    def __repr__(self):
        """
        Return representation of Rectangle.
        """
        wth = str(eval('self.width'))
        hght = str(eval('self.height'))

        return 'Rectangle(' + wth + ', ' + hght + ')'
