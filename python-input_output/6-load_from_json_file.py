#!/usr/bin/python3
"""Create object from a JSON file"""
import json


def load_from_json_file(filename):
    """function that creates an Object from a “JSON file"""
    with open(filename, encoding='utf-8') as myFile:
        return json.loads(myFile.read())
