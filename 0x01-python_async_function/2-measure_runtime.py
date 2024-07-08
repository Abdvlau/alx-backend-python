#!/usr/bin/env python3
"""
In the file 2-measure_runtime.py, import the wait_n function from the
previous file.

Create a new function called measure_time that takes two integer arguments,
n and max_delay. This function should measure the total execution time for
calling wait_n(n, max_delay) and return the average execution time per call,
calculated as total_time / n. The function should return a float.

Use the time module to measure the approximate elapsed time.
"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Measuring the runtime """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
