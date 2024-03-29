#!/usr/bin/python3
"""
Contain class BaseGeometry
"""


class BaseGeometry:
    """class with public instance methods area and integer_validator"""
    def area(self):
        """raises an exception if called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ To confirm if value is integer greater than 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
