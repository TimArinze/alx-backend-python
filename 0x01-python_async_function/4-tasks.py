#!/usr/bin/env python3
"""
Tasks
"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Execute multiple coroutines at the same time"""
    routines = [task_wait_random(max_delay) for _ in range(n)]
    allRoutines = await asyncio.gather(*routines)
    return sorted(allRoutines)
