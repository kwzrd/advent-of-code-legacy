# Reference: https://adventofcode.com/2020/day/9

import itertools
import typing as t

Stream = t.List[int]


def satisfies(num: int, preamble: Stream) -> bool:
    """True if `num` is a valid successor of `preamble`."""
    for a, b in itertools.combinations(preamble, r=2):
        if a + b == num:
            return True

    return False


def part_one(stream: Stream, p_size: int) -> int:
    """Find first number in `stream` that doesn't satisfy preamble of `p_size`."""
    for i, num in enumerate(stream[p_size:], start=p_size):
        if not satisfies(num, stream[i - p_size:i]):
            return num

    raise Exception("Solution not found!")


def part_two(stream: Stream, violation: int) -> int:
    """Find the sum of min & max in the sequence that sums to `violation`."""
    for start in range(len(stream) - 1):
        for end in range(start + 2, len(stream) + 1):
            seq = stream[start:end]
            seq_sum = sum(seq)
            if seq_sum == violation:
                return min(seq) + max(seq)
            if seq_sum > violation:
                break  # No point in going further, since the sum can only grow

    raise Exception("Solution not found!")


def main(input_data: str) -> t.Tuple[int, int]:
    """Solution entry-point."""
    stream = [int(n) for n in input_data.splitlines()]

    invalid = part_one(stream, p_size=25)
    seq_sum = part_two(stream, invalid)

    return invalid, seq_sum
