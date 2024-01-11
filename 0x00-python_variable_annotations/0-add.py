#!/usr/bin/env python3
"""
    Type-annotated function add
"""


def add(a: float, b: float) -> float:
    """Takes 2 floats and returns their sum as float"""
    if isinstance(a, float) and isinstance(b, float):
        return float(a + b)
    raise TypeError('Enter float values')
