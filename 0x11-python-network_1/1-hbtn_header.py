#!/usr/bin/python3
""" Fetches header from url passed as arg"""
from urllib import request
import sys

with request.urlopen(sys.argv[1]) as response:
    print(response.getheader("X-Request-Id"))
