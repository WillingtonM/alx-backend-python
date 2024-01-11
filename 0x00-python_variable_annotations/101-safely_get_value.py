#!/usr/bin/env python3
"""
    Safely get a dictionary value by key
"""
from typing import Any, Mapping, TypeVar, Union
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None]
                     = None) -> Union[Any, T]:
    """Function to safely get a dictionary value given a key"""
    if key in dct:
        return dct[key]
    else:
        return default
