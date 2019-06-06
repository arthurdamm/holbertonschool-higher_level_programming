#!/usr/bin/python3
'''Module for from_json_string method.'''
import json


def from_json_string(my_str):
    '''Method for loading object from json string.'''
    return json.loads(my_str)
