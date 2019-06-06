#!/usr/bin/python3
'''Module for read_lines method.'''


def read_lines(filename="", nb_lines=0):
    '''Method for reading lines from file.'''
    with open(filename, "r") as f:
        if nb_lines <= 0:
            print(f.read(), end="")
            return

        for line in f:
            print(line, end="")
            nb_lines -= 1
            if nb_lines <= 0:
                break
