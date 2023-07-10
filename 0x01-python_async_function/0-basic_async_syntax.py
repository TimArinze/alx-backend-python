#!/usr/bin/env python3
"""
Basics of async
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Returns at random float time"""
    delay_time = random.uniform(0, max_delay)
    await asyncio.sleep(delay_time)
    return delay_time
