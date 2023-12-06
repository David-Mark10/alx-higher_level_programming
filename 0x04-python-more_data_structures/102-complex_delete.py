#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    val_to_delete = []

    for val in a_dictionary:
        if a_dictionary[val] == value:
            val_to_delete.append(val)

    for val in val_to_delete:
        del a_dictionary[val]

    return a_dictionary
