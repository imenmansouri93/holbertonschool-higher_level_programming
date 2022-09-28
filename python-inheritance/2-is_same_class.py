#!/usr/bin/python3
"""check function"""


def is_same_class(obj, a_class):
    """returns True if the obj is exactly an instance of the specified class"""
    return type(obj) is a_class
