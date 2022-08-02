#!/usr/bin/python3
"""
This module contain one function, read_file(filename="")
"""


def read_file(filename=""):
    """
    reade the text file encoded with UTF-8.

    and prints it out to stdout
    """
    with open(filename) as f:
        content = f.read()
        print(content, end="")
