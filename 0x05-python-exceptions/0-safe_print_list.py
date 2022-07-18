#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        result = my_list[:x]
        result_holder =  ''.join(str(e) for e in result)
        return int(result_holder)
    except IndexError:
        result_holder = ''.join(str(e) for e in my_list)
        return int(result_holder)
