#!/usr/bin/python3
"""Base class"""
import json


class Base:
    """Represent class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    def to_json_string(list_dictionaries):
        """Dictionary to JSON string"""
        if list_dictionaries is None or len(list_dictionaries) is 0:
            return ("[]")
        else:
            json_object = json.dumps(list_dictionaries)
            return(json_object)

    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file

        Args:
            list_objs (list): list of instances who inherits of Base
        """
        with open(cls.__name__ + '.json', 'w', encoding='utf-8') as myFile:
            if list_objs is None:
                myFile.write("[]")
            else:
                myFile.write(cls.to_json_string([item.to_dictionary()
                        for item in list_objs]))

    def from_json_string(json_string):
        """from json to string"""
        if json_string is None or len(json_string) is 0:
            return ([])
        else:
            return(json.loads(json_string))
