#!/usr/bin/env python3
"""
Duck typing - first element of a sequence
"""
from typing import Sequence, Union, Any, Optional, NoneType


def safe_first_element(lst: Sequence[Any]) -> Union[Any, NoneType]:
    """Duck-typed annotation"""
    if lst:
        return lst[0]
    else:
        return None
