#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    ret = []
    while i < list_length:
        try:
            res = my_list_1[i] / my_list_2[i]
        except (ZeroDivisionError, TypeError, IndexError):
            res = 0
        finally:
            ret.append(res)
            i += 1
    return ret
