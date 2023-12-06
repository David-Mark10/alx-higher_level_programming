#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    numb = sum(n * m for n, m in my_list)
    deg = sum(m for n, m in my_list)

    return numb / deg
