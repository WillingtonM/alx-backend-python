#!/usr/bin/env python3
"""
    Type-annotated function sum_list
"""
from typing import List
from functools import reduce


def sum_list(input_list: List[float]) -> float:
    """
        Takes list of floats & returns their sum as float
    """
    if not isinstance(input_list, list):
        raise TypeError("expected a list as input")
    return float(reduce(lambda x, y: x + y, input_list))


if __name__ == "__main__":
    print(sum_list([1, 2, 3, 4]))
