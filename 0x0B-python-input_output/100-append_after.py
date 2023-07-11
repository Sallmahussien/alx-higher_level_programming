#!/usr/bin/python3
'''Defines append_after function'''


def append_after(filename="", search_string="", new_string=""):
    '''Inserts a line of text to a file,
       after each line containing a specific string
    '''

    with open(filename, encoding='utf-8') as file:
        lines = file.readlines()

    for idx, line in enumerate(lines):
        if search_string in line:
            lines.insert(idx + 1, new_string)

    with open(filename, 'w', encoding='utf-8') as file_write:
        file_write.writelines(lines)
