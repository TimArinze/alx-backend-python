#!/usr/bin/env python3
"""
Complex types - mixed list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """takes int and float then returns sum as float"""
    accumulator = 0.0
    for number in mxd_lst:
        accumulator += float(number)
    return accumulator
