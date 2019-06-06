#!/usr/bin/python3
'''Module for append_write method.'''


def append_write(filename="", text=""):
    '''Method for reading lines from file.'''
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
