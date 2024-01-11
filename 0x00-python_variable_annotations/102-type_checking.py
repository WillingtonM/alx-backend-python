#!/usr/bin/env python3
"""
    This module provides function to zoom in on array
"""
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Zoom in array upto factor number of times"""
    zoomd_in: List = [
        x for x in lst
        for y in range(int(factor))
    ]
    return zoomd_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
