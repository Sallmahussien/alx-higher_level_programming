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
    if hasattr(obj, '__slots__') and attr_name not in obj.__slots__:
        raise TypeError("can't add new attribute")

    obj.__dict__[attr_name] = attr_value
