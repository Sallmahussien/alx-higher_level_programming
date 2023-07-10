#!/usr/bin/python3
'''Defines lookup function'''


def lookup(obj):
    '''Returns the list of available attributes and methods of an object

    Args:
        obj (object): an object

    Return:
        list of an instance attributes and methods
    '''
    return dir(obj)
