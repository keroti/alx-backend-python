#!/usr/bin/env python3
"""
Function to anntoniate the arguments to get right results
"""

from typing import Any, List, Union


def safe_first_element(lst: List[Any]) -> Union[Any, None]:
    """
    Duck-typed function that returns the first element of a sequence
    """
    if lst:
        return lst[0]
    else:
        return None
