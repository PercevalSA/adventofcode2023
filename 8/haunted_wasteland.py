#!/usr/bin/python3

from itertools import cycle

direction = {"L": 0, "R": 1}


# parse str like AAA = (BBB, CCC)
# left is 0 and right 1 in tuple
def parse_node(node: str) -> tuple[str, tuple[str, str]]:
    item, directions = node.split("=")
    directions = directions.strip()
    dirs = (directions[1:4], directions[-4:-1])  # get only letters
    return item.strip(), dirs


def parse_input(data: str) -> tuple[str, dict]:
    parsed = data.splitlines()
    instructions = parsed.pop(0)
    parsed.pop(0)  # empty line

    map = {}
    for line in parsed:
        item, directions = parse_node(line)
        map[item] = directions

    return instructions, map


def iterate_instructions(instructions: str, map: dict, start: str, destination: str):
    iterator = cycle(instructions)
    location = start
    step = 0

    print("start:", location)
    while location != destination:
        move_to = next(iterator)
        print("move to:", move_to)
        location = map[location][direction[move_to]]
        print("location :", location)
        step += 1

    print(step)
    return step


def solve_part_1(data: str) -> int:
    instructions, map = parse_input(data)
    return iterate_instructions(instructions, map, "AAA", "ZZZ")


def main(file: str):
    with open(file, "r") as f:
        data = f.read()

    result = solve_part_1(data)
    print(f"Result 1: {result}")


if __name__ == "__main__":
    main("8/input.txt")
