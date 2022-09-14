#!/usr/bin/python3
from copy import copy


def divisible_by_2(my_list=[]):
     A = my_list.copy()
     for i in range(len(A)):
        if A[i] % 2 == 0:
            A[i] = True
        else:
            A[i] = False
        return (A)
