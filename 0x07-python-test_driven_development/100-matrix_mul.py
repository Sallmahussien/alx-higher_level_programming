#!/usr/bin/python3
'''Defines matrix_mul function'''


def matrix_mul(m_a, m_b):
    '''Multiplies 2 matrices

    Args:
        m_a (list of lists): fisrt matrix
        m_ab (list of lists): second matrix

    Raises:
        TypeError: when m_a or m_b are not lists
                   when m_a or m_b are not list of lists
                   when elements of m_a or m_b are not int or float
                   when rows of m_a or m_b have no the same size
        ValueError: when m_a or m_b empty
                    when m_a and m_b can't be multiplied

        ValueError

    Return:
        The multiplication of the two matrices
    '''
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError('m_a must be a list of lists')
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError('m_b must be a list of lists')

    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")

    if not all(isinstance(n, (int, float)) for r in m_a for n in r):
        raise TypeError('m_a should contain only integers or floats')
    if not all(isinstance(n, (int, float)) for r in m_b for n in r):
        raise TypeError('m_b should contain only integers or floats')

    length_of_1st_row = len(m_a[0])
    if not all(length_of_1st_row == len(row) for row in m_a):
        raise TypeError('each row of m_a must be of the same size')

    length_of_1st_row = len(m_b[0])
    if not all(length_of_1st_row == len(row) for row in m_b):
        raise TypeError('each row of m_b must be of the same size')

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for j in range(len(m_b[0]))] for i in range(len(m_a))]
    for i, row_a in enumerate(m_a):
        for j, col_b in enumerate(zip(*m_b)):
            result[i][j] = sum([a * b for a, b in zip(row_a, col_b)])

    return result
