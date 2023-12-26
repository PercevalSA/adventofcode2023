#!/usr/bin/python3


def parse_data(data: str) -> list[str]:
    return data.splitlines()


def solve_part_1(data: list[str]) -> int:
    return 0


def main(file: str):
    with open(file, "r") as f:
        data = f.read()

    parsed = parse_data(data)

    result = solve_part_1(parsed)
    print(f"Result 1: {result}")


if __name__ == "__main__":
    main("10/input.txt")
