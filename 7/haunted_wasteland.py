#!/usr/bin/python3


def parse_input(data: str) -> list:
    return data.splitlines()


def solve_part_1(data: list):
    return 0


def main(file: str):
    with open(file, "r") as f:
        data = f.read()

    parsed_data = parse_input(data)
    result = solve_part_1(parsed_data)
    print(f"Result 1: {result}")


if __name__ == "__main__":
    main("7/input.txt")
