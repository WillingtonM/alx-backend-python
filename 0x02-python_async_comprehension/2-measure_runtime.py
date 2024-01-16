#!/usr/bin/env python3
"""
Runtime for parallel comprehensions
"""
import asyncio
import time
from importlib import import_module as using


async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension 4 times and measures execution time.
    """
    start_tm = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_tm