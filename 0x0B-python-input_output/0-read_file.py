#!/usr/bin/python3
"""
A function that read_file
"""


def read_file(filename=""):
    """reads a file(UTF8) and prints it to stdout"""
    with open(filename, "r", encoding="utf-8") as fil:
        print(fil.read(), end="")
