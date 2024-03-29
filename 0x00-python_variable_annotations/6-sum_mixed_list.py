#!/usr/bin/env python3

"""A type annotated 'sum_mixed_list' function"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    a type-annotated function sum_mixed_list which takes a
    list mxd_lst of integers and floats and returns their sum as a float.
    """
    total: float = 0
    for element in mxd_lst:
        total += float(element)
    return total
