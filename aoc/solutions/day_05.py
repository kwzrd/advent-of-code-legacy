# Reference: https://adventofcode.com/2020/day/5

import typing as t


def decode(boarding_pass: str) -> int:
    """Calculate `boarding_pass` ID."""
    boarding_pass = boarding_pass.translate(str.maketrans("FBLR", "0101"))

    row = int(boarding_pass[:7], base=2)
    col = int(boarding_pass[7:], base=2)

    return row * 8 + col


def main(input_data: str) -> t.Tuple[int, int]:
    """Solution entry-point."""
    passes = {decode(line) for line in input_data.splitlines()}
    mi, ma = min(passes), max(passes)

    return ma, sum(range(mi, ma + 1)) - sum(passes)
