#!/usr/bin/python3
"""
This module contains the function that adds two number
This module supplies only one function, add_integer(a, b)
"""


def add_integer(a, b=98):
    """
    This function returns two integers, Given two integers.
    :param a: int, float
    :param a: int, float
    :return: int
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    elif type(b) not in (int, float):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
