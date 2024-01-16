#!/usr/bin/env python3
"""
Module that execute multiple coroutines at same time with async
"""
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay
    returns: list of all delays.
    """
    futrs = [wait_random(max_delay) for _ in range(n)]
    futrs = asyncio.as_completed(futrs)
    delys = [await future for future in futrs]
    return delys
