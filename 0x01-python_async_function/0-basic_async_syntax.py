#!/usr/bin/env python3
"""
Basics of async
"""
import asyncio
import random


async def wait_random(max_delay=10):
    """Returns at random float time"""
    delay_time = random.random() * max_delay
    await asyncio.sleep(delay_time)
    return delay_time
