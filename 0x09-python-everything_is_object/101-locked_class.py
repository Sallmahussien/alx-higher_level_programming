#!/usr/bin/python3
'''Defines a class LockedClass '''


class LockedClass:
    '''The implementation of LockedClass class'''
    __slots__ = ['first_name']

    def __init__(self, first_name=''):
        '''Initialize a new instance from class LockedClass'''
        self.first_name = first_name
