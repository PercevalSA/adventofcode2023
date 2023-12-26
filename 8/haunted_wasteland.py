#!/usr/bin/python3

import math
from itertools import cycle

direction = {"L": 0, "R": 1}


# parse str like AAA = (BBB, CCC)
# left is 0 and right 1 in tuple
def parse_node(node: str) -> tuple[str, tuple[str, str]]:
    item, directions = node.split("=")
    directions = directions.strip()
    dirs = (directions[1:4], directions[-4:-1])  # get only letters
    return item.strip(), dirs


def parse_input(data: str) -> tuple[str, dict[str, tuple[str, str]]]:
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

    while location != destination:
        move_to = next(iterator)
        location = map[location][direction[move_to]]
        step += 1

    return step


def solve_part_1(data: str) -> int:
    instructions, map = parse_input(data)
    return iterate_instructions(instructions, map, "AAA", "ZZZ")


def get_all_starting_locations(map: dict) -> list[str]:
    return [k for k in map.keys() if k[-1] == "A"]


def solve_part_2(data: str) -> int:
    instructions, map = parse_input(data)
    iterator = cycle(instructions)
    locations = get_all_starting_locations(map)
    step = 0

    while not all([item[-1] == "Z" for item in locations]):
        move_to = next(iterator)
        for i in range(len(locations)):
            locations[i] = map[locations[i]][direction[move_to]]
        step += 1
    print(locations)
    return step


def try_part_2(data: str) -> int:
    instructions, map = parse_input(data)
    locations = get_all_starting_locations(map)

    steps: list[int] = []
    for start in locations:
        local = start
        print(local)
        iterator = cycle(instructions)
        step = 0

        while not local[-1] == "Z":
            move_to = next(iterator)
            local = map[local][direction[move_to]]
            step += 1
        print(local)
        print(step)
        steps.append(step)

    return math.lcm(*steps)


def main(file: str):
    with open(file, "r") as f:
        data = f.read()

    result = solve_part_1(data)
    print(f"Result 1: {result}")

    result = try_part_2(data)
    print(f"TRY 2: {result}")


if __name__ == "__main__":
    main("8/input.txt")
