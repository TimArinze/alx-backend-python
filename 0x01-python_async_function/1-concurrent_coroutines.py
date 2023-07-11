#!/usr/bin/env python3
"""
Let execute multiple coroutines at the same time with async
"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Execute multiple coroutines at the same time"""
    routines = [wait_random(max_delay) for _ in range(n)]
    allRoutines = await asyncio.gather(*routines)
    return sorted(allRoutines)
