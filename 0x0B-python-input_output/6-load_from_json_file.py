#!/usr/bin/python3
"""
A function "load_from_json_file" that load json file 
"""

import json


def load_from_json_file(filename):

    with open(filename, 'r', encoding='utf-8') as fil:
        return json.load(fil)
