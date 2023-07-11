#!/usr/bin/python3
'''Defines write_file function'''


def write_file(filename="", text=""):
    '''Writes a string to a text file (UTF8)

    Args:
        filename (string): file name
        text (string): text to be written to a file

    Return:
        The number of characters written
    '''
    with open(filename, 'w', encoding='utf-8') as file:
        num_chars = file.write(text)

    return num_chars
