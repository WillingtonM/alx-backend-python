#!/usr/bin/env python3
"""
    Defines duck typed function
"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Get the first element in a sequence safely
    If the there's no elements, return None
    """
    if lst:
        return lst[0]
    else:
        return None
