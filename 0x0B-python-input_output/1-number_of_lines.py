#!/usr/bin/python3
'''Module for number_of_lines method.'''


def number_of_lines(filename=""):
    '''Method for reading from file.'''
    num = 0
    with open(filename, "r") as f:
        lines = f.readlines()
        num = len(lines)
        if lines[-1][-1] != "\n":
            num -= 1
    f.close()
    return num
