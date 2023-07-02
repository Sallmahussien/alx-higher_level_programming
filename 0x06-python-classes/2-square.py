#!/usr/bin/python3
'''Define a class Square.'''


class Square:
    '''The implementation of a Square class'''
    def __init__(self, size=0):
        '''Initialize a new Square

        Args:
            size (int): Defines the size of new Square
        '''
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
