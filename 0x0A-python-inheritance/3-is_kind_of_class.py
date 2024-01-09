#!/usr/bin/python3
"""
the function is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """if obj is instance, True or inherited from a_class, else False"""
    return (isinstance(obj, a_class))
