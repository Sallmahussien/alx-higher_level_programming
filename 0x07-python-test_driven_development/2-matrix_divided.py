#!/usr/bin/python3
'''Defines matrix_divided function that divides all elements of a matrix.'''


def matrix_divided(matrix, div):
    '''Divides all elements of a matrix

    Args:
        matrix (list of lists): 2d matrix
        div (int): number to be divided by the matrix

    Raises:
        TypeError: when the matrix is not a list of lists
                   when length of lists are n't equal to each other
                   when each element in th matrix isn't int or float
        ZeroDivisionError: when div == 0

    Return:
        A new matrix
    '''
    is_2d_matrix = all(isinstance(row, list) for row in matrix)
    is_valid_type = all(isinstance(n, (int, float)) for r in matrix for n in r)
    if not (isinstance(matrix, list) and is_2d_matrix and is_valid_type):
        err_msg = 'matrix must be a matrix (list of lists) of integers/floats'
        raise TypeError(err_msg)

    length_of_1st_row = len(matrix[0])
    if not all(length_of_1st_row == len(row) for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    div_matrix = [[round(val / div, 2) for val in row] for row in matrix]

    return div_matrix
