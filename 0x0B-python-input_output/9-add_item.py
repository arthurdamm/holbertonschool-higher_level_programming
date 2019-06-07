#!/usr/bin/python3
'''Module for saving argv info via json to file.'''
import json
import os.path
import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

file = "add_item.json"
json_list = []
try:
    json_list = load_from_json_file(file)
except:
json_list = []
    
for i in range(1, len(sys.argv)):
    json_list.append(sys.argv[i])

save_to_json_file(json_list, file)
