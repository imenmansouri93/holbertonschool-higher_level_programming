#!/usr/bin/python3
"""defines the lookup functions"""


def lookup(obj):
    """returns the list of available attributes and methods of an object"""
    return(dir(obj))