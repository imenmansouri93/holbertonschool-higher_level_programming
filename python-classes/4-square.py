#!/usr/bin/python3
"""Define a square with private instance"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """initialise  variable
        Args:
        size (int): The size of the new square.
        """
        self.__size = size
        """retrieve size"""
    @property
    def size(self):
        return self.__size
    """set private size attribute """
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    """Public instance method"""
    def area(self):
        """returns the current square area"""
        return(self.__size * self.__size)
