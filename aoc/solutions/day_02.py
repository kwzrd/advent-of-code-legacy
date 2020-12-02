import re
import typing as t

RE_CONSTRAINT = re.compile(r"(\d+)-(\d+) ([a-z]): ([a-z]+)")

Constraint = t.Tuple[int, int, str, str]


def parse_constraints(input_data: str) -> t.List[Constraint]:
    """Parse `input_data` into a list of `Constraint` tuples."""
    constraints = []

    for line in input_data.splitlines():
        n1, n2, char, password = RE_CONSTRAINT.match(line).groups()
        constraints.append((int(n1), int(n2), char, password))

    return constraints


def part_one(constraints: t.List[Constraint]) -> int:
    """
    Count `constraints` for part one.

    Lines where `char` occurs at least `low` and at most `high` times.
    """
    n_valid = 0

    for low, high, char, password in constraints:
        n_valid += low <= password.count(char) <= high

    return n_valid


def part_two(constraints: t.List[Constraint]) -> int:
    """
    Count `constraints` for part two.

    Lines where `char` occurs at exactly one of the two indices.
    """
    n_valid = 0

    for i1, i2, char, password in constraints:
        n_valid += (password[i1 - 1] == char) is not (password[i2 - 1] == char)

    return n_valid


def main(input_data: str) -> t.Tuple[int, int]:
    """Solution entry-point."""
    constraints = parse_constraints(input_data)

    return part_one(constraints), part_two(constraints)
