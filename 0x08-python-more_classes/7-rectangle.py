#!/usr/bin/python3
'''Defines the class Rectangle'''


class Rectangle:
    '''The implementation of the Rectangle class'''

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        '''Initialize a new instance from class Rectanle'''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        '''Retrieves the new Rectangle width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Sets the new Rectangle width'''
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        '''Retrieves the new Rectangle height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Sets the new Rectangle height'''
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value

    def area(self):
        '''Calculate the new Rectangle area'''
        return self.width * self.height

    def perimeter(self):
        '''Returns the new Rectangle perimeter'''
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        '''Return a str for the rectangle with the character #'''
        if self.width == 0 or self.height == 0:
            return ""

        rect = ''
        for _ in range(self.height):
            rect += ('{}'.format(str(self.print_symbol)) * self.width)
            rect += '\n'
        rect = rect.strip('\n')

        return rect

    def __repr__(self) -> str:
        '''Return a string representation of the rectangle to
           be able to recreate a new instance by using eval()'''
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        '''Prints a msg when deleting an instance'''
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')
