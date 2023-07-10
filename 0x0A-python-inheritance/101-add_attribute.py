#!/usr/bin/python3
'''Defines add_attribute function'''


def add_attribute(obj, attr_name, attr_value):
    '''Adds a new attribute to an object if it's possible.

    Args:
        obj (object): an object
        attr_name (str): attribute name
        attr_value (str): attribute value

    Exceptions:
        TypeError: If the object can't have new attribute
    '''
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    setattr(obj, attr_name, attr_value)
