#!/usr/bin/env python3
"""
Let duck type an iterable object
"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Annotate it all"""
    return [(i, len(i)) for i in lst]
