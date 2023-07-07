#!/usr/bin/env python3
"""
Complex types - string and int/float to tuple
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Takes str for first element and int or float for the second
        then returns a Tuple of str as first element and float or int as
        second element
    """
    square = v * v
    return (k, square)
