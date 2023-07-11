#!/usr/bin/python3
'''Defines read_file function'''


def read_file(filename=""):
    '''Reads a text file (UTF8) and prints it to stdout

    Args:
        filename (string): the file name
    '''

    with open(filename, encoding="utf-8") as file:
        for line in file:
            print(line, end='')
