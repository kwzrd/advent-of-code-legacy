# Reference: https://adventofcode.com/2020/day/8

import typing as t

Instruction = t.Tuple[str, int]
Program = t.List[Instruction]


def execute(program: Program) -> t.Tuple[bool, int]:
    """
    Execute `program` returning final accumulator state.
    First return value determines whether the program halted normally.
    """
    visited_states = set()
    acc = state = 0

    while state not in visited_states:
        visited_states.add(state)

        try:
            op, value = program[state]
        except IndexError:
            return True, acc  # Stepping out of the program means normal halt

        if op == "jmp":
            state += value
        else:
            if op == "acc":
                acc += value
            state += 1

    return False, acc  # We detected a cycle & aborted execution


def mutations(program: Program) -> t.Iterable[Program]:
    """Generate possible mutations of `program`."""
    switch = {"jmp": "nop", "nop": "jmp"}

    for i, (op, value) in enumerate(program):
        if new_op := switch.get(op):
            mutation = program.copy()
            mutation[i] = (new_op, value)
            yield mutation


def main(input_data: str) -> t.Tuple[int, int]:
    """Solution entry-point."""
    program: Program = []

    for instruction in input_data.splitlines():
        op, value = instruction.split()
        program.append((op, int(value)))

    _, part_one = execute(program)

    for mutation in mutations(program):
        halted_normally, part_two = execute(mutation)
        if halted_normally:
            break
    else:
        raise Exception("No valid mutation found")

    return part_one, part_two
