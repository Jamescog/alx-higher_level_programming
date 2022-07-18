#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        number = 0
        result = my_list[:x]
        for i in result:
            number += 1
        result_holder = ''.join(str(e) for e in result)
        print(result_holder)
        return number
    except IndexError:
        return None
