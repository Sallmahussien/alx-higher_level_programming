#!/usr/bin/python3
'''Defines Square class'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Implement Square class'''
    def __init__(self, size, x=0, y=0, id=None):
        '''Initialize an instance from Square class'''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''Gets the Square width'''
        return self.width

    @size.setter
    def size(self, value):
        '''Sets the Square size'''
        self.width = value
        self.height = value

    def __str__(self):
        '''Return a printable representation of the Square class'''
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.size))

    def update(self, *args, **kwargs):
        '''Assigns attributes'''
        args_len = len(args)
        if args_len != 0:
            if args_len >= 1:
                self.id = args[0]
            if args_len >= 2:
                self.width = args[1]
            if args_len >= 3:
                self.x = args[2]
            if args_len >= 4:
                self.y = args[3]
        elif len(kwargs) != 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''Returns the dictionary representation of a Square'''
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
