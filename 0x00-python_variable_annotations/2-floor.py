#!/usr/bin/env python3
"""
    Type-annotated function floor
"""

def floor(n: float) -> int:
    """
        Returns floor of float passed to it
    """
    if not isinstance(n, float):
        raise TypeError('An invalid parameter passed, float was expected')
    return int(n)
