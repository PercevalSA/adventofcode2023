#!/usr/bin/python3


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


def solve_part_1(data: list) -> int:
    return 0


def main(file: str):
    with open(file, "r") as f:
        data = f.read()

    parsed_data = parse_input(data)
    result = solve_part_1(parsed_data)
    print(f"Result 1: {result}")


if __name__ == "__main__":
    main("8/input.txt")
