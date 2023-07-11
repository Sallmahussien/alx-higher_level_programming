#!/usr/bin/python3
'''Defines load_from_json_file function'''
import json


def load_from_json_file(filename):
    '''Creates an Object from a "JSON file"'''
    with open(filename, encoding='utf-8') as file:
        return json.load(file)
