#!/usr/bin/python3
"""Real definition of a rectangle"""


class Rectangle():
    """Represent a Rectangle"""
    def __init__(self, width=0, height=0):
        """
        Create a new rectangle of width  and height.
        Args:
            width (int): The width of a new rectangle:
            height (int): The height of the new rectangle:
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width of the rectangle
        Args:
            value(int): new value for width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        set the height of the rectangle
        Args:
            valu (int): new value for height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
