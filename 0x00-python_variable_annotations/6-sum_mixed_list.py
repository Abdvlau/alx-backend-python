#!/usr/bin/env python3
"""A module that sums up list of ints"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """sums a list of ints
    args:
        mxd_lst (list) a list of ints
    Returns a sum of floats
    """
    return sum(mxd_lst)
