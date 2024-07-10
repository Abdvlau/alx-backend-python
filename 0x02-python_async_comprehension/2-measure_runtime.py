#!/usr/bin/env python3
"""Four asynchronous Comprehension operation"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Create a list of 10 random numbers
    using asynchronous comprehension
    and return the resulting list
    """

    start_time: float = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time: float = time.perf_counter()
    return (end_time - start_time)
