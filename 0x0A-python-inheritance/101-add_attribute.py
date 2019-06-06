#!/usr/bin/python3
'''Module for add_attribute method.'''


def add_attribute(obj, name, value):
    '''Method that tests if it can and sets an attribute.'''
    if hasattr(obj, name) or not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
