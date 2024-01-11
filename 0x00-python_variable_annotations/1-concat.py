#!/usr/bin/env python3
"""
    Type-annotated function concat
"""

def concat(str1: str, str2: str) -> str:
    """Takes 2 str variables & returns their concatenation"""
    if isinstance(str1, str) and isinstance(str2, str):
        return f"{str1}{str2}"
    raise TypeError("Only strings should be passed")
