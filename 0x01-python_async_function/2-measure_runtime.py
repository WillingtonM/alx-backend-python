#!/usr/bin/env python3
"""
Module that compute average excetion time for running subroutine
"""
from asyncio import run
from time import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure excetution time of subroutine
    return: float
    """
    start_time = time()

    run(wait_n(n, max_delay))

    end_time = time()

    return (end_time - start_time) / n
