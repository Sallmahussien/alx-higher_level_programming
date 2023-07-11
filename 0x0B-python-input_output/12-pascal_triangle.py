#!/usr/bin/python3
'''Defines pascal_triangle function'''


def pascal_triangle(n):
    '''Returns a list of lists representing the Pascal's triangle of n'''

    if n <= 0:
        return []

    pascal_list = [[0 for j in range(i + 1)] for i in range(n)]

    for r_idx, row in enumerate(pascal_list):
        row[0] = 1
        row[len(row) - 1] = 1
        for idx in range(1, len(row) - 1):
            row[idx] = (pascal_list[r_idx - 1][idx - 1]
                        + pascal_list[r_idx - 1][idx])

    return pascal_list
