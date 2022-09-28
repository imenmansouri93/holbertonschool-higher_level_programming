#!/usr/bin/python3
"""Rectangle
"""
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

class Rectangle(BaseGeometry):
    """class Rectangle that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("width", height)
        self.__height = height