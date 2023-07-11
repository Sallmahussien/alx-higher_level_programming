#!/usr/bin/python3
'''Defines Student class'''


class Student:
    '''Implement Student class'''
    def __init__(self, first_name, last_name, age):
        '''Initialize a new instance from Student class'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''Retrieves a dictionary representation of a Student instance'''
        if attrs is None or not all(isinstance(ele, str) for ele in attrs):
            return self.__dict__

        new_dict = {}
        for key in attrs:
            if hasattr(self, key):
                new_dict[key] = getattr(self, key)
        return new_dict

    def reload_from_json(self, json):
        '''Replaces all attributes of the Student instance'''
        for key, value in json.items():
            setattr(self, key, value)
