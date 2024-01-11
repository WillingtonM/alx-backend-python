#!/usr/bin/env python3
"""
    Type-annotated function sum_mixed_list
"""
from typing import List, Union
from functools import reduce


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
        Accepts mixed list of integers & floats & returns
        their sum as float
    """
    a: float = 0.0
    for x in mxd_lst:
        a += x
    return a
