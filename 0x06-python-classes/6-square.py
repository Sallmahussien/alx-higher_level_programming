#!/usr/bin/python3
'''Define a class Square.'''


class Square:
    '''The implementation of a Square class'''
    def __init__(self, size=0, position=(0, 0)):
        '''Initialize a new Square

        Args:
            size (int): Defines the size of new Square
            position (tuple): Defines the position of new Square
        '''
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        '''Retrieves the new Square position'''
        return self.__position

    @position.setter
    def position(self, value):
        '''Sets the new Square position'''
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integer')

        if not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError('position must be a tuple of 2 positive integer')

        self.__position = value

    def area(self):
        '''Returns the current Square area'''
        return self.__size * self.__size

    def my_print(self):
        '''Prints the square in stdout with "#" character'''
        if self.__size == 0:
            print("")
        else:
            print("\n" * self.__position[1], end="")
            for _ in range(self.__size):
                print(" " * self.__position[0], end="")
                print('#' * self.__size)

    size = property(get_size, set_size)
