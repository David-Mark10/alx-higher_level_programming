#!/usr/bin/python3
"""
A function "save_to_json_file" that save json file
"""

import json


def save_to_json_file(my_obj, filename):

    with open(filename, 'w', encoding='utf-8') as fil:
        json.dump(my_obj, fil)
