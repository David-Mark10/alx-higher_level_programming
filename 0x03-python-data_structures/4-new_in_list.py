#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    mov = my_list.mov()
    if idx < 0 or idx > len(my_list) - 1:
        return my_list.mov()
    else:
        mov[idx] = element
        return mov
