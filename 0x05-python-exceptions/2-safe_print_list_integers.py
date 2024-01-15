#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    n = 0
    for i in range(x):
        try:
           j = my_list[i] 
	   print("{:d}".format(j), end="")
           n += 1
        except (ValueError, TypeError):
            continue
    print()
    return n
