import numpy as np


def is_part_number(position: int) -> bool:
    return False


def parse_data(data: str) -> np.array:
    table = [[letter for letter in line] for line in data.splitlines()]
    return np.array(table)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = f.read()
    print(parse_data(data))
