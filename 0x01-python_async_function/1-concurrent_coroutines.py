#!/usr/bin/env python3
"""Import the wait_random function from a previous Python file.
Then, create an asynchronous function named wait_n that accepts
two integer arguments: max_delay and n. Within wait_n,
invoke wait_random asynchronously n times,
each time with the provided max_delay.
The function should return a list containing all delay values (floats),
arranged in ascending order based on completion time,
without using sort() due to concurrent execution.
 """


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Executing multiple coroutines at the same time with async  """
    delays: List[float] = []
    all_delays: List[float] = []
    for i in range(n):
        delays.append(wait_random(max_delay))
    for delay in asyncio.as_completed(delays):
        earliest_result = await delay
        all_delays.append(earliest_result)
    return all_delays
