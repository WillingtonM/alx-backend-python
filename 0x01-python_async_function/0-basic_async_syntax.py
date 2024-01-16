#!/usr/bin/env python3

"""
Concurent programming in python using asyncio library
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Couroutine waits for random number of seconds
    returns: number of seconds waited
    """
    if not isinstance(max_delay, int):
        raise TypeError('Max wait should be an int')
    wait_tm = random.random() * max_delay
    await asyncio.sleep(wait_tm)
    return wait_tm
