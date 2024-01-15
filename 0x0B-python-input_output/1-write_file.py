#!/usr/bin/python3
"""
A function that "wrtie_file"
"""


def write_file(filename="", text=""):
    """returns the number of chars written to "filename" from "text" """
    with open(filename, 'w', encoding='utf=8') as fil:
        return fil.write(text)
