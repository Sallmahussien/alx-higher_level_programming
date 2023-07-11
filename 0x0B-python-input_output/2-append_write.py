#!/usr/bin/python3
'''Defines append_write function'''


def append_write(filename="", text=""):
    '''Appends a string at the end of a text file (UTF8)

    Args:
        filename (string): file name
        text (string): text to be written

    Return:
        the number of characters added
    '''
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
