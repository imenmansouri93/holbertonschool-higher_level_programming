#!usr/bin/python3
"""Define a square"""
class Square:
    """Represent square"""
    def __init__(self, size=0):
        self.__size = size
    """retrieve size """
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
        """return crrent square area"""
        return(self.__size * self.__size)
    """public instance method"""
    def my_print(self):
        """ prints in stdout the square with the character #"""
        for i in range (self.__size):
            for j in range(self.__size):
                print("#",end="")
            print("")
        if self.__size <= 0:
            print("")
