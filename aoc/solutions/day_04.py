# Reference: https://adventofcode.com/2020/day/4

import re
import typing as t

RE_FIELD = re.compile(r"([a-z]{3}):(\S+)")

RE_HCL = re.compile(r"#[a-f0-9]{6}")
RE_PID = re.compile(r"\d{9}")


def in_range(num: str, mi: int, ma: int) -> bool:
    """True if `num` between `mi` and `ma` inclusive & ignoring all non-digit chars."""
    clean = "".join(char for char in num if char.isdigit())
    return int(clean) in range(mi, ma + 1)


REQUIRED = {
    "byr": lambda x: in_range(x, 1920, 2002),
    "iyr": lambda x: in_range(x, 2010, 2020),
    "eyr": lambda x: in_range(x, 2020, 2030),
    "hgt": lambda x: x.endswith("cm") and in_range(x, 150, 193) or x.endswith("in") and in_range(x, 59, 76),
    "ecl": lambda x: x in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"},
    "hcl": lambda x: bool(RE_HCL.fullmatch(x)),
    "pid": lambda x: bool(RE_PID.fullmatch(x)),
}


def main(input_data: str) -> t.Tuple[int, int]:
    """Solution entry-point."""
    part_one = part_two = 0

    for batch in input_data.split("\n\n"):
        passport = dict(RE_FIELD.findall(batch))

        if not REQUIRED.keys() <= passport.keys():
            continue

        part_one += 1
        part_two += all(check(passport[key]) for key, check in REQUIRED.items())

    return part_one, part_two
