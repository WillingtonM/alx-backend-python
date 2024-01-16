#!/usr/bin/env python3

""""
Module that creates a task
"""
from asyncio import Task, create_task


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """
    wait for random number of some seconds
    return: asyncio Task
    """
    return create_task(wait_random(max_delay))
