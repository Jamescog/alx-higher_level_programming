#!/usr/bin/python3
"""
This module contains one function, to_json_string(my_obj)
Argumets:
    :param my_obj : string
Return:
    return JSON representation
"""


def to_json_string(my_obj):
    """
    This function accept and object
    and returns JSON representation
    """
    import json
    return json.dumps(my_obj)
