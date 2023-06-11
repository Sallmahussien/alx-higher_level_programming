#!/usr/bin/python3

def max_integer(my_list=[]):

    if len(my_list) == 0:
        return None

    max_num = my_list[0]
    for idx in range(1, len(my_list)):
        if my_list[idx] > max_num:
            max_num = my_list[idx]

    return (max_num)
