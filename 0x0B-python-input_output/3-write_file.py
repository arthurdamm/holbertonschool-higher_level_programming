#!/usr/bin/python3
'''Module for read_lines method.'''


def write_file(filename="", text=""):
    '''Method for reading lines from file.'''
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
