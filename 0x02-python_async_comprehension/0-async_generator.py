#!/usr/bin/env python3
"""
Module with async generator
"""

from typing import Generator
from random import random
from asyncio import sleep


async def async_generator() -> Generator[float, None, None]:
    """
    Generate numbers between 1 and 10
    Returns: Generator
    """
    for _ in range(0, 10):
        await sleep(1)
        yield random() * 10
