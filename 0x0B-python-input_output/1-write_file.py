#!/usr/bin/python3
"""
This module contain one function, write_file(filename="", text="")
It supplies a function that write a string to a text file
"""


def write_file(filename="", text=""):
    """
    a function that writes a string to a text file
    Return the number of characters written
    """
    num = len(text)
    with open(filename,'w', encoding = "utf-8") as wf:
        writing = wf.write(text)
    return num
