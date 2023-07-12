#!/usr/bin/python3
'''Defines append_after function'''


def append_after(filename="", search_string="", new_string=""):
    '''Inserts a line of text to a file,
       after each line containing a specific string
    '''

    with open(filename, 'r+', encoding='utf-8') as file:
        lines = file.readlines()

        new_list = []
        for line in lines:
            new_list.append(line)
            if search_string in line:
                new_list.append(new_string)

        file.seek(0)
        file.write("".join(new_list))
