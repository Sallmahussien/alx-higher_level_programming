#!/usr/bin/python3
'''Defines text_indentation function'''


def text_indentation(text):
    ''' Prints a text with 2 new lines after each of these
        characters: ., ? and :

    Args:
        text (str): the text to be printed

    Raises:
        TypeError: when the is not str
    '''

    if not isinstance(text, str):
        raise TypeError('text must be a string')

    new_text_list = text.split(' ')
    new_text_list = [element for element in new_text_list if element != '']
    new_text = ' '.join(new_text_list)
    new_text = (new_text.strip()
                .replace('. ', '.').replace('.', '.\n\n')
                .replace('? ', '?').replace('?', '?\n\n')
                .replace(': ', ':').replace(':', ':\n\n')
                )

    print(new_text, end='')
