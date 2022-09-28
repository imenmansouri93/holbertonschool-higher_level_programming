#!/usr/bin/python3
"""Integer validator"""


class BaseGeometry:
    """Represent BaseGeometry
    """
    def area(self):
        """not implemented"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
            if not isinstance(value, int):
                raise TypeError ("<name> must be an integer")
            if value <= 0:
                raise ValueError ("<name> must be greater than 0")
