#!/usr/bin/env python3
"""
    Type-annotated function floor
"""


def to_str(n: float) -> str:
    """Takes float & returns its str repr"""
    if not isinstance(n, float):
        raise TypeError('Invalid argument passed, expected a float')
    return str(n)
