#!/usr/bin/python3
""" Uses requests module to get header info"""
import requests
from sys import argv

if __name__ == "__main__":
    response = requests.get(argv[1], data={'email': argv[2]})
    print(response.text)
