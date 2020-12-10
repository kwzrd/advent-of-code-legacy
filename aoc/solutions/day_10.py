# Reference: https://adventofcode.com/2020/day/10

import typing as t
from collections import defaultdict


def main(input_data: str) -> t.Tuple[int, int]:
    """Solution entry-point."""
    adapters = sorted(int(adapter) for adapter in input_data.splitlines())
    adapters = [0] + adapters + [max(adapters) + 3]  # Add the outlet & my device

    differences = defaultdict(int)

    for i in range(len(adapters) - 1):
        d = adapters[i + 1] - adapters[i]
        differences[d] += 1

    variations = defaultdict(int, {0: 1})  # Prime with the first connection

    for adapter in adapters[1:]:
        for back_step in range(1, 3 + 1):
            variations[adapter] += variations[adapter - back_step]

    return differences[1] * differences[3], variations[max(adapters)]
