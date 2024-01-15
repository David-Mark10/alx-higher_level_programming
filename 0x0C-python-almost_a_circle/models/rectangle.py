#!/usr/bin/python3
"""

"""
import base

class Rectangle(Base):
    """

    """
    def __init__(self, width, height, x=0, y=0):
        """
         Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init_

         @property
    def width(self):
        """Set/get width of Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Set/get height of Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Set/get x coordinate of Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Set/get y coordinate of Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return area of Rectangle."""
        return self.width * self.height

    def display(self):
        """Print Rectangle using `#` character."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """Update the Rectangle.

        Args:
            *args (ints): The new attributes value.
                - the 1st argument represents the id attribute
                - the 2nd argument represents the width attribute
                - the 3rd argument represent the height attribute
                - the 4th argument represents the x attribute
                - the 5th argument represents the y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            j = 0
            for arg in args:
                if j == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif j == 1:
                    self.width = arg
                elif j == 2:
                    self.height = arg
                elif j == 3:
                    self.x = arg
                elif j == 4:
                    self.y = arg
                j += 1

        elif kwargs and len(kwargs) != 0:
            for n, u in kwargs.items():
                if n == "id":
                    if u is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = u
                elif n == "width":
                    self.width = u
                elif n == "height":
                    self.height = u
                elif n == "x":
                    self.x = u
                elif n == "y":
                    self.y = u

    def to_dictionary(self):
        """Return dict representation of Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return print() and str() representation of Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)




