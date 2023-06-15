#!/usr/bun/python3


def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    sum_tuple, denominator = 0, 0

    for my_tuple in my_list:
        sum_tuple += (my_tuple[0] * my_tuple[1])
        denominator += my_tuple[1]

    return (sum_tuple / denominator)
