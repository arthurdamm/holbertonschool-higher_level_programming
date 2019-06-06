#!/usr/bin/python3
'''Module for class_to_json method.'''


def class_to_json(obj):
    '''Returns dictionary description of json object.'''
    return obj.__dict__
