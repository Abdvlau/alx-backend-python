#!/usr/bin/env python3
"""A module with a coroutine that takes no argument  """
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """A coroutine that loops 10 times
    asynchronously wait for 1 second
    then yiled a random number between 0 & 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
