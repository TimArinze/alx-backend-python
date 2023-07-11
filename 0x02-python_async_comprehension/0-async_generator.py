#!/usr/bin/env python3
"""
Async Generator
"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator:
    """loop 10 times each time waits for 1 second
        yields a random number from 0 - 10
    """
    for _ in range(0, 10):
        random_number = random.uniform(0, 10)
        await asyncio.sleep(1)
        yield random_number
