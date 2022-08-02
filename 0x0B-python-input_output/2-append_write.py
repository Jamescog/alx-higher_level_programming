#!/usr/bin/python3
"""
This module contains one function,append_write(filename="", text="")
appends a string at the end of a text file (UTF8)
return the number of characters added
"""


def append_write(filename="", text=""):
    """
    The function that appends a string at the end of a text file(utf-8)
    Returns the number of characters added
    """
    num = len(text)
    with open(filename, 'a', encoding="utf-8") as wf:
         wf.write(text)
    return num
