#!/usr/bin/env python3
"""
Complex types - list of floats
"""


Sum = list[float]


def sum_list(input_list: Sum) -> float:
    """sum of list of float"""
    accumulator = 0
    for x in input_list:
        accumulator += x
    return accumulator
