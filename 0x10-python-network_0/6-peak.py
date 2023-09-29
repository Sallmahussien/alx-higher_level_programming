#!/usr/bin/python3
"""Implementation of find_peak function"""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers."""

    if not list_of_integers or list_of_integers == []:
        return None

    length = len(list_of_integers)
    first_max = list_of_integers[0]
    second_max = list_of_integers[length - 1]

    for idx in range(1, length // 2):
        first_max = max(first_max, list_of_integers[idx])
        second_max = max(second_max, list_of_integers[length - idx - 1])

    return max(first_max, second_max)


def max(first_value, second_value):
    """Return max of two integeres"""
    if first_value >= second_value:
        return first_value
    return second_value
