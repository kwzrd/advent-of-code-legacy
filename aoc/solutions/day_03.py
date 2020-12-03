# Reference: https://adventofcode.com/2020/day/3

import math
import typing as t

Coordinates = t.Tuple[int, int]  # Height & width indices


class Map:
    """
    Wrapper around the input data.

    Subscriptable for convenient access via height & width indices.
    """

    def __init__(self, area: str) -> None:
        """Slice data & pre-compute max height & width."""
        self.area = area.split("\n")[:-1]  # Trailing newline leaves an annoying empty string
        self.max_h = len(self.area)
        self.max_w = len(self.area[0])

    def __getitem__(self, coordinates: Coordinates) -> str:
        """Access item by height & width index tuple."""
        h, w = coordinates
        return self.area[h][w % self.max_w]


def solve_for(m: Map, slope: Coordinates) -> int:
    """Count tree occurrences when traversing `m` on `slope`."""
    n_trees = h = w = 0
    h_step, w_step = slope

    while h < m.max_h:
        n_trees += m[h, w] == "#"
        h += h_step
        w += w_step

    return n_trees


def main(input_data: str) -> t.Tuple[int, int]:
    """Solution entry-point."""
    m = Map(input_data)

    part_one = solve_for(m, (1, 3))
    part_two = math.prod([
        solve_for(m, slope)
        for slope in [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    ])

    return part_one, part_two
