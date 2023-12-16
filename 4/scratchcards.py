#!/usr/bin/python3


def parse_data(data: str) -> list:
    return [line for line in data.splitlines()]


def solve_part_1(data):
    return True


def main(file: str):
    with open(file, "r") as f:
        data = f.read()
    parsed_data = parse_data(data)

    result = solve_part_1(parsed_data)
    print(f"Result 1: {result}")


if __name__ == "__main__":
    main("4/input.txt")
