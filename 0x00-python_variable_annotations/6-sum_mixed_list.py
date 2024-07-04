#!/usr/bin/env python3
"""A module that sums up list of ints"""
from typing import List


def sum_mixed_list(mxd_lst: List[int]) -> float:
    """sums a list of ints
    args:
        mxd_lst (list) a list of ints
    Returns a sum of floats
    """
    if mxd_lst is None:
        return 0
    else:
        return sum(mxd_lst)
