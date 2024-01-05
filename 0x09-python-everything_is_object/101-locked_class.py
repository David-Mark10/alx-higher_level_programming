#!/usr/bin/python3
class LockedClass:
    """
        A class with only one attribute.
        Attribute:
             first_name (str): name
    """
    __slots__ = ['first_name']
