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

    new_text = (text.strip()
                .replace('. ', '.\n\n')
                .replace('? ', '?\n\n')
                .replace(': ', ':\n\n'))
    print(new_text, end='')
