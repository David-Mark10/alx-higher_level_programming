#!/usr/bin/python3
def search_replace(my_list, search, replace):
    nw_list = []
    for item in my_list:
        if item == search:
            nw_list.append(replace)
        else:
            nw_list.append(item)
    return nw_list
