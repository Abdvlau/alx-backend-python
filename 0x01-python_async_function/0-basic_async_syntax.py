#!/usr/bin/env python3
"""This module contains an asynchronous """
import random


async def wait_random(max_delay=10):
    """This function take an argument
    that waits for a random delay and
    eventually return it
    """
    delay = random.uniform(0, max_delay)

    return delay
