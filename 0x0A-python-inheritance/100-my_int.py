#!/usr/bin/python3
'''Defines MyInt class'''


class MyInt(int):
    '''implement MyInt class'''

    def __eq__(self, other):
        '''Reverse the behaviour of __eq__'''
        return super().__ne__(other)

    def __ne__(self, other):
        '''Reverse the behaviour of __ne__'''
        return super().__eq__(other)
