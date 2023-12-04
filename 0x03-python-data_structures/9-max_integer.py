#!/usr/bin/python3
# 9-max_integer.py

def max_integer(my_list=[]):

    if not my_list:
        return None

    bgt = my_list[0]
    for n in my_list:
        if n > bgt:
            bgt = n

    return bgt
