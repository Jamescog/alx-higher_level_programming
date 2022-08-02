#!/usr/bin/python3
"""
This module contains one function, from_json_string(my_str)
it accepts JSON and return Python standard data sturcture
"""
def from_json_string(my_str):
    """
    The function that returns an object from JSON
    """
    import json
    return json.loads(my_str)
