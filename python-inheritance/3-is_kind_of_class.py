#!/usr/bin/python3
"""check function"""


def is_kind_of_class(obj, a_class):
    """returns True if the object
    is an instance of,or if the object
    is an instance of a class that inherited from class
    """
    return isinstance(obj, a_class)
