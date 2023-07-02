#!/usr/bin/python3
'''Define a class Square.'''


class Square:
    '''The implementation of a Square class'''
    def __init__(self, size=0):
        '''Initialize a new Square

        Args:
            size (int): Defines the size of new Square
        '''
        self.__size = size

    def get_size(self):
        '''Getting the size of the new Square'''
        return self.__size

    def set_size(self, value):
        '''Setting the size of the new Square'''
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        '''Returns the current Square area'''
        return self.__size * self.__size

    def my_print(self):
        '''Prints the square in stdout with "#" character'''
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print('#' * self.__size)

    size = property(get_size, set_size)
