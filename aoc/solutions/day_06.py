# Reference: https://adventofcode.com/2020/day/6

import typing as t


def main(input_data: str) -> t.Tuple[int, int]:
    """Solution entry-point."""
    groups = [[set(person) for person in group.splitlines()] for group in input_data.split("\n\n")]
    part_one = part_two = 0

    for group in groups:
        part_one += len(set.union(*group))
        part_two += len(set.intersection(*group))

    return part_one, part_two
