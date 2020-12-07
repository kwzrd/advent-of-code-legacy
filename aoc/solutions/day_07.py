# Reference: https://adventofcode.com/2020/day/7

import re
import typing as t

RE_LHS = re.compile(r"^(\w+ \w+)")
RE_RHS = re.compile(r"(\d) (\w+ \w+)")

BagMap = t.Dict[str, t.Dict[str, int]]  # Bag name to its contents


def contains(bag_map: BagMap, key: str, search_term: str) -> bool:
    """True if `search_term` is reachable from `key`."""
    children = bag_map[key]  # Immediate children
    return search_term in children or any(contains(bag_map, child, search_term) for child in children)


def deep_sum(bag_map: BagMap, key: str) -> int:
    """Recursive sum of `key` and and all its children."""
    immediate = sum(bag_map[key].values())  # Amount of immediate children
    return immediate + sum(times * deep_sum(bag_map, key) for key, times in bag_map[key].items())


def main(input_data: str) -> t.Tuple[int, int]:
    """Solution entry-point."""
    bag_map: BagMap = {}

    for line in input_data.splitlines():
        lhs, *_ = RE_LHS.findall(line)
        bag_map[lhs] = {name: int(count) for count, name in RE_RHS.findall(line)}

    part_one = sum(contains(bag_map, key, "shiny gold") for key in bag_map)
    part_two = deep_sum(bag_map, "shiny gold")

    return part_one, part_two
