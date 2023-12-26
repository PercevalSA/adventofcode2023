#!/usr/bin/python3


def parse_data(data: str) -> list[list[int]]:
    splitted = data.splitlines()
    parsed = [[int(i) for i in line.split()] for line in splitted]
    return parsed


def get_steps(values: list[int]) -> list[int]:
    return [values[i + 1] - values[i] for i in range(len(values) - 1)]


def solve_part_1(data: str) -> int:
    return 0


def main(file: str):
    with open(file, "r") as f:
        data = f.read()

    result = solve_part_1(data)
    print(f"Result 1: {result}")


if __name__ == "__main__":
    main("9/input.txt")
