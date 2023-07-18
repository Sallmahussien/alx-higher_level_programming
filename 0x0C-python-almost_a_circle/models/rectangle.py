#!/usr/bin/python3
'''Defines Rectangle class'''
from models.base import Base


class Rectangle(Base):
    '''Implement Rectangle class'''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''Initialize a new instance from Rectangle class'''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''Retrieves the width of the new Rectangle'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Sets the width of the new Rectangle'''
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        '''Gets the height of the new Rectangle'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Sets the height of the new Rectangle'''
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        '''Gets the x of the new Rectangle'''
        return self.__x

    @x.setter
    def x(self, value):
        '''Sets the x of the new Rectangle'''
        if type(value) != int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        '''Gets the y of the new Rectangle'''
        return self.__y

    @y.setter
    def y(self, value):
        '''Sets the y of the new Rectangle'''
        if type(value) != int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        '''Returns the area of the rectangle'''
        return self.width * self.height

    def display(self):
        '''Prints in stdout the Rectangle instance with the character #'''
        print("\n" * self.y, end='')
        for _ in range(self.height):
            print(" " * self.x, end='')
            print('#' * self.width)

    def __str__(self):
        '''Return a printable representation of the rectangle'''
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        '''Assigns attributes'''
        args_len = len(args)
        if args_len != 0:
            if args_len >= 1:
                self.id = args[0]
            if args_len >= 2:
                self.width = args[1]
            if args_len >= 3:
                self.height = args[2]
            if args_len >= 4:
                self.x = args[3]
            if args_len >= 5:
                self.y = args[4]
        elif len(kwargs) != 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''Returns the dictionary representation of a Rectangle'''
        return {"id": self.id, "width": self.width,
                "height": self.height, "x": self.x, "y": self.y}
