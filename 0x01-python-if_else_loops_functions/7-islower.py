#include "lists.h"
/**
 * islower - A function that checks for lowercase
 * @c: the function argument to be checked
 *
 * @Return: return true if lowercase or false if upercase
def islower(c):
    # Indent the code inside the function
    if len(c) == 1:
        chrt = ord(c)
        if chrt >= 97 and chrt <= 122:
            return True
    else:
        return False
