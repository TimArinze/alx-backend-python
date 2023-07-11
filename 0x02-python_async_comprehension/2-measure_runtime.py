#!/usr/bin/env python3
"""
Run time for four parallel comprehension
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures the total runtime and returns it"""
    start_time = time.time()
    routine = [async_comprehension() for _ in range(4)]
    routines = await asyncio.gather(*routine)
    end_time = time.time()
    return end_time - start_time
