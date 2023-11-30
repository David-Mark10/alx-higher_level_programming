#!/usr/bin/python3
/**
 *print_last_digit - A function that prints last digit
 *@number: The digit number to print 
 *@Return: return the last value of the number
 */

def print_last_digit(number):
    lnumb = abs(number) % 10
    print(lnumb, end="")
    return lnumb
