# Reference: https://adventofcode.com/2020/day/1

import itertools
import math
import typing as t


def solve_for(numbers: t.List[int], n_factors: int) -> int:
    """
    Find the product of `numbers` which add up to 2020.

    Give `n_factors` the amount of numbers to try to combine.
    """
    for combination in itertools.combinations(numbers, r=n_factors):
        if sum(combination) == 2020:
            return math.prod(combination)

    raise Exception("No solution found")


def main(input_data: str) -> t.Tuple[int, int]:
    """Solution entry-point."""
    numbers = [int(n) for n in input_data.split()]

    return solve_for(numbers, n_factors=2), solve_for(numbers, n_factors=3)
