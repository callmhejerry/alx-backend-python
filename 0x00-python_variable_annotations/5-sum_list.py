#!/usr/bin/env python3

"""A type annotated function 'sum_list'"""


from typing import List


def sum_list(input_lists: List[float]) -> float:
    """
    a type-annotated function sum_list which takes a list input_list
    of floats as argument and returns their sum as a float
    """
    total: float = 0.0
    for element in input_lists:
        total += element
    return total
