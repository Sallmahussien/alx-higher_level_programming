#!/usr/bin/python3
'''Defines Square class'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Implement Square class'''
    def __init__(self, size):
        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        '''Calculate the area of the BaseGeometry instance'''
        return self.__size * 2
