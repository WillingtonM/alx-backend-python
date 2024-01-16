#!/usr/bin/env python3
"""
Module that execute multiple coroutines at same time with async
"""
from typing import List
import asyncio


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executive wait_random n times with specified max_delay
    returns: list of all delays.
    """
    futrs = [task_wait_random(max_delay) for _ in range(n)]
    futrs = asyncio.as_completed(futrs)
    delys = [await future for future in futrs]
    return delys
