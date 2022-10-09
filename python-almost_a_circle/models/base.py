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
