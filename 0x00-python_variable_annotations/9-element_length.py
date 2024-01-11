#!/usr/bin/env python3
"""
Type-annotated function element_length
"""
from typing import Iterable, List, Sequence, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns list of tuples of sequence & int"""
    return [(l, len(l)) for l in lst]
