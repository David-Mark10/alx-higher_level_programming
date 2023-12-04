#!/usr/bin/python3

def no_c(my_string):

    data = ""
    for char in my_string:
        if char.lower() != 'c':
            data += char
    return data
