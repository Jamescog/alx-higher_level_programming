#!/usr/bin/python3
"""
This module contain one function, save_to_json_file(my_obj, filename)
create(overwrite) a file and write and obj to a txt file
in JSON represantation
"""


def def save_to_json_file(my_obj, filename):
    """
    This function writes an Object to a txt file
    using JSON represantation
    """
    import json
    obj = json.dumps(my_obj)
    with open(filename, "w", encoding="utf-8") as wf:
        wf.write(obj)
