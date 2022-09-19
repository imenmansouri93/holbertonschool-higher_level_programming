#!/usr/bin/python3
"""Define a square with private instance"""


class Square:
    """Represent a square"""

    def __init__(self, size):
        """initialise  variable
        Args:
        size (int): The size of the new square.
        """
        self.__size = size
