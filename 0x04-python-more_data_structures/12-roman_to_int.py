#!/usr/bin/python3
def to_subtract(list_num):
    totl = 0
mx_lst = max(list_num)

    for j in list_num:
        if mx_lst > j:
            totl += j

    return mx_list - totl


def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0

    rom_numb = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    numb = lst_rom = lst_num = 0

    for chrt in roman_string:
        if chrt not in rom_numb:
            return 0

        crnt_rom = rom_numb[chrt]

        if crnt_rom <= lst_rom:
            numb += to_subtract(lst_num)
            lst_num = [crnt_rom]
        else:
            lst_num.append(crnt_rom)

        lst_rom = crnt_rom

    numb += to_subtract(lst_num)

    return (numb)
