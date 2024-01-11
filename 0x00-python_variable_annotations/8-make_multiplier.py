#!/usr/bin/env python3
"""
    function make_multiplier: Type-annotated
"""
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns function that multiplies float"""
    return lambda x: x * multiplier
