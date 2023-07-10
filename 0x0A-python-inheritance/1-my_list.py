#!/usr/bin/python3
'''Defines MyList class'''


class MyList(list):
    '''Initialize MyList class that inherits from list'''

    def print_sorted(self):
        '''Prints the list, but sorted (ascending sort)'''
        print(sorted(self))
