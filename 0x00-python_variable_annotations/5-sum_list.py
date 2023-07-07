#!/usr/bin/env python3
"""
Complex types - list of floats
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """sum of list of float"""
    accumulator = 0
    for x in input_list:
        accumulator += x
    return accumulator
