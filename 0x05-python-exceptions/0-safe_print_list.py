#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        result = my_list[:x]
        return result
    except IndexError:
        return my_list
