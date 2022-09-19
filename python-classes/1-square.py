#!/usr/bin/python3
"""Define a sqare with private instance"""


class Square:
    def __init__(self, size):
        """initialise  variable
        Args:
        size (int): The size of the new square.
        """
        self.__size = size
