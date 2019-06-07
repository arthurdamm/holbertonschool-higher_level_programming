#!/usr/bin/python3
'''Module for log parsing script.'''
import sys
import re

size = 0
codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
rex = re.compile(
    '(\S+) - \[([^]]+)\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)\n')


def check_match(line):
    '''Checks for regexp match in line.'''
    global size
    match = rex.search(line)
    if not match:
        return
    size += int(match.group(4))
    code = int(match.group(3))
    if code in codes:
        codes[code] += 1


def print_stats():
    '''Prints accumulated statistics.'''
    print("File size: {}".format(size))
    for k in sorted(codes.keys()):
        if codes[k]:
            print("{}: {}".format(k, codes[k]))
i = 1
while True:
    try:
        r = sys.stdin.readline()
        if r == "":
            break
    except KeyboardInterrupt:
        print_stats()
    check_match(r)
    if i % 10 == 0:
        print_stats()
    i += 1
