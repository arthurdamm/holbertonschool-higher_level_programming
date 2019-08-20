#!/usr/bin/python3
"""Finds peak in unsorted list of integers"""


def find_peak(list_of_integers):
    """Finds peak in unsorted list of integers"""
    for i, n in enumerate(list_of_integers):
        if i < len(list_of_integers) - 1 and n < list_of_integers[i + 1]:
            continue
        return n
    return None
