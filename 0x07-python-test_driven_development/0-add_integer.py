#!/usr/bin/python3
'''Defines add_integer function that adds two integers'''


def add_integer(a, b=98):
    '''Adds two integers

    Args:
        a (int): first integer
        b (int): second integer

      Return: addition of a and b,
              or raise an error if one of them isn't int or floar'''
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')

    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')

    return int(a) + int(b)
