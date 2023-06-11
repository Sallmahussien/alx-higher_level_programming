#!/usr/bin/python3

def no_c(my_string):
    list_str = [char for char in my_string if char not in "Cc"]
    new_str = "".join(list_str)
    return new_str
