#!/usr/bin/env python3


"""A type annotated 'make_multiplier' functino"""
from collections.abc import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    a type-annotated function make_multiplier that takes a float
    multiplier as argument and returns a function that multiplies a
    float by multiplier.
    """
    def inner_function(second_multiplier: float) -> float:
        return multiplier * second_multiplier

    return inner_function
