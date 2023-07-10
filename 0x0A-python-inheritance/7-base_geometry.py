#!/usr/bin/python3
'''Defines BaseGeometry class'''


class BaseGeometry:
    '''The implementation of BaseGeometry class'''
    def area(self):
        '''Calculate the area of the BaseGeometry instance'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''Validates value

        Args:
            name (str): name
            vale (int): value

        Exceptions:
            TypeError: when the value isn't integer
            ValueError: when the value is smaller than or equal 0
        '''
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
