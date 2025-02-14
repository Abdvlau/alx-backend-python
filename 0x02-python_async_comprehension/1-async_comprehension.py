#!/usr/bin/env python3
"""Defines a coroutine """
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """A coroutine that takes no argument
    collect 10 random numbers using an async comprehensing over
    then return the 10 random numbers.
    """
    return [number async for number in async_generator()]
