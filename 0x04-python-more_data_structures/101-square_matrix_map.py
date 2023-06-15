#!/usr/bin/python3


def square_matrix_map(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_matrix.append(list(map(lambda num: num ** 2, row)))
    return new_matrix
