#!/usr/bin/python3
"""
Write a function that returns the dictionary description
with simple data structure (list, dictionary, string, 
integer and boolean)for JSON serialization of an objec
"""


def class_to_json(obj):
    return obj.__dict__
