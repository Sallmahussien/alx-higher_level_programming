#!/usr/bin/python3
'''Defines Base class'''

import json
import os
import csv


class Base:
    '''Implement Base class'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''Base class constructor'''
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts a list of dictionaries to a JSON string representation"""
        if not list_dictionaries or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''Writes the JSON string representation of list_objs to a file

        Args:
            list_objs: is a list of instances who inherits of Base
        '''
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        with open(filename, 'w', encoding='utf-8') as file:
            list_objs = [obj.to_dictionary() for obj in list_objs]
            file.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        ''' Returns the list of the JSON string representation

        Args:
            json_string: is a string representing a list of dictionarie
        '''
        if json_string is None or json == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''Returns an instance with all attributes already set'''
        if cls.__name__ == "Square":
            new_instance = cls(1)
        else:
            new_instance = cls(1, 1)
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        '''Returns a list of instances'''
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []
        with open(filename, encoding='utf-8') as file:
            dict_list = cls.from_json_string(file.read())

        instsance_list = [cls.create(**dictionary) for dictionary in dict_list]
        return instsance_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''Writes the CSV string representation of list_objs to a file

        Args:
            list_objs: is a list of instances who inherits of Base
        '''

        filename = cls.__name__ + ".csv"

        with open(filename, 'w', encoding='utf-8') as csv_file:
            if list_objs is None or list_objs == []:
                csv_file.write("[]")
            else:
                list_objs = [obj.to_dictionary() for obj in list_objs]
                if cls.__name__ == "Rectangle":
                    fieldnames = ['id', 'width', 'height', 'x', 'y']
                else:
                    fieldnames = ['id', 'size', 'x', 'y']
                csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

                csv_writer.writeheader()
                for obj in list_objs:
                    csv_writer.writerow(obj)

    @classmethod
    def load_from_file_csv(cls):
        '''Retuens list of instances from CSV file'''
        filename = cls.__name__ + ".csv"
        if not os.path.exists(filename):
            return []
        with open(filename, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            instsance_list = []
            for dictionary in csv_reader:
                dictionary = {k: int(v) for k, v in dictionary.items()}
                instsance_list.append(cls.create(**dictionary))
        return instsance_list
