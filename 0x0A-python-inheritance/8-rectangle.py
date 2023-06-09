#!/usr/bin/python3
'''Defines Rectangle class'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Implement the Rectangle class'''

    def __init__(self, width, height):
        '''Initialize a new instancle from Rectangle class'''
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height
