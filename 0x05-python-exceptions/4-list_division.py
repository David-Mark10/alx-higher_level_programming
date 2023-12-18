#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_lst = []
    for j in range(list_length):
        try:
            output = my_list_1[j] / my_list_2[j]
        except (ValueError, TypeError):
            print("wrong type")
            output = 0
        except ZeroDivisionError:
            print("division by 0")
            output = 0
        except IndexError:
            print("out of range")
            output = 0
        finally:
            new_lst.append(output)
    return new_lst
