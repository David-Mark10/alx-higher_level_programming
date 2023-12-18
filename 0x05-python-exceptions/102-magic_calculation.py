#!/usr/bin/python3

def magic_calculation(a, b):
    output = 0
    for j in range(1, 3):
        try:
            if j > a:
                raise Exception('Too far')
            else:
                output += a ** b / j
        except Exception:
            output = b + a
            break
    return output
