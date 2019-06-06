#!/usr/bin/python3
'''Module for save_to_json_file method.'''
import json


def save_to_json_file(my_obj, filename):
    '''Method for saving json file.'''
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
