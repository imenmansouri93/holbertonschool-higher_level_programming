#!/usr/bin/python3
"""define a class named MyLits"""
class MyList(list):
    """ class named MyList
    attr1(print_sorted) : printed sorted list
    """
    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
