#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = list(a_dictionary.keys())
    keys.sort()
    for k in keys:
        print("{}: {}".format(k, a_dictionary[k]))
