#!/usr/bin/python3
"""Module containing inherits_from method"""


def inherits_from(obj, a_class):
    """if the object is instance of a class, return True then
    inherited (directly or indirectly) from the specified class;
    otherwise False"""
    return isinstance(obj, a_class) and type(obj) != a_class
