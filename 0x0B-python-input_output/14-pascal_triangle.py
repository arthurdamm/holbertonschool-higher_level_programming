#!/usr/bin/python3
'''Module for pascal_triangle method.'''


def pascal_triangle(n):
    '''Method that solves pascal's triangle.'''
    ret = [0 for i in range(n)]
    # ret[0] = list_prev
    for n in range(n):
        list_curr = [1 for i in range(n + 1)]
        for i in range(n - 1):
            list_curr[i + 1] = sum(list_prev[i:i + 2])
        ret[n] = list_curr
        list_prev = list_curr
    return ret
