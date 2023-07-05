#!/usr/bin/python3
'''Defines print_square function that prints a square with the character #'''


def print_square(size):
    '''Prints a square with the character #

    Args:
        size (int): the square size

    Raises:
        TypeError: when the size isn't integer
                   when the size is float smaller than zero
        ValueError: when the size is int and less than zero
    '''

    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    for _ in range(size):
        print('#' * size)
