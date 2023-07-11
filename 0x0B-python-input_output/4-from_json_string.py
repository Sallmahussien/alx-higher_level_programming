#!/usr/bin/python3
'''Defines from_json_string function'''
import json


def from_json_string(my_str):
    '''Returns a python object represented by a JSON string'''
    return json.loads(my_str)
