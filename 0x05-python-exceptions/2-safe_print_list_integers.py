#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    printed_elements = 0

    for idx in range(x):
        try:
            print("{:d}".format(my_list[idx]), end="")
            printed_elements += 1
        except (ValueError, TypeError):
            continue

    print("")

    return printed_elements
