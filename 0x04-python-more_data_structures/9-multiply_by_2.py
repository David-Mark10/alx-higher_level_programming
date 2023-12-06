#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    nw_dir = a_dictionary.copy()

    for key in nw_dir:
        nw_dir[key] *= 2

    return nw_dir
