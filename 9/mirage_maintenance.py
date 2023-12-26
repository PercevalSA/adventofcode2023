#!/usr/bin/python3


def parse_data(data: str) -> list[list[int]]:
    splitted = data.splitlines()
    parsed = [[int(i) for i in line.split()] for line in splitted]
    return parsed


def get_steps(values: list[int]) -> list[int]:
    plop = [values[i + 1] - values[i] for i in range(len(values) - 1)]
    print(plop)
    return plop


def generate_all_steps(values: list[int]) -> list[list[int]]:
    all_steps = [values]

    while not all([item == 0 for item in all_steps[-1]]):
        all_steps.append(get_steps(all_steps[-1]))

    return all_steps


def solve_part_1(data: str) -> int:
    return 0


def main(file: str):
    with open(file, "r") as f:
        data = f.read()

    result = solve_part_1(data)
    print(f"Result 1: {result}")


if __name__ == "__main__":
    main("9/input.txt")
