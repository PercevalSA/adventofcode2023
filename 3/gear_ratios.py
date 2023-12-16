#!/usr/bin/python3


# for each nuber found extract all surrounding chars and join as a string
# then find symbols in string to detect of it is a part number
# To avoid having to check for borders and hitting them
# we add an extra border of dots around the input
# we will store the grid in a dict in order to take advantage of defaultdict
# def default_factory() -> str:
#     return "."
# we will use setdefault((x,y), ".") instead of get because
# default factory does not handle tuple as key


from typing import Generator


def parse_data_as_dict(data: str) -> dict:
    table = {}
    for y, line in enumerate(data.splitlines()):
        for x, letter in enumerate(line):
            table[(x, y)] = letter
    return table


def get_all_num_positions(table: dict) -> Generator:
    for i in table:
        if table[i].isnumeric():
            yield i


def get_number_len(position: tuple[int, int], table: dict) -> int:
    len = 0
    # iterate on the line and check if the char is int, increase len
    # if we find something else return the len because the nulmber has ended
    # we use try except because we cannot levrage defaultvalue because it changes dict
    # while we are iterating generating an error
    try:
        while table.get((position[0] + len, position[1])).isnumeric():
            len += 1
    except AttributeError:
        pass
    return len


def get_all_numbers_with_size(table: dict) -> dict[tuple[int, int], int]:
    nums_with_size = {}
    all_nums = iter(get_all_num_positions(table))
    for num in all_nums:
        size = get_number_len(num, table)
        for _ in range(1, size):
            next(all_nums)
        nums_with_size[num] = size

    return nums_with_size


def get_number(position: tuple[int, int], size: int, table: dict) -> int:
    number = ""
    for i in range(size):
        number += str(table.get((position[0] + i, position[1])))
    return int(number)


def extract_surroundings(position: tuple, len: int, table: dict) -> str:
    surroundings = ""
    for y in range(position[1] - 1, position[1] + 2):
        for x in range(position[0] - 1, position[0] + len + 1):
            surroundings += str(table.setdefault((x, y), "."))

    return surroundings


def is_part_number(surrounding: str) -> bool:
    for i in surrounding:
        if not i.isnumeric() and i != ".":
            return True

    return False


def solve_part_1(data: dict) -> int:
    # get all nums before we sort and extract part nums
    all_nums = get_all_numbers_with_size(data)

    # extract only part nums
    result = 0
    for num in all_nums:
        num_size = get_number_len(num, data)
        if is_part_number(extract_surroundings(num, num_size, data)):
            result += get_number(num, num_size, data)

    return result


# PART 2
#
# A gear is any * symbol that is adjacent to exactly two part numbers.
# Its gear ratio is the result of multiplying those two numbers together.
def is_gear_ratio(position: tuple):
    """find the numbers around the stars and return true if 2 are present"""
    return False


def find_gear_ratios(position: tuple):
    return False


def find_all_gear(table: dict) -> Generator:
    for char in table:
        if table.get(char) == "*":
            yield char


def main(file: str):
    with open(file, "r") as f:
        data = f.read()
    parsed_data = parse_data_as_dict(data)

    result = solve_part_1(parsed_data)
    print(f"Result 1: {result}")


if __name__ == "__main__":
    main("3/input.txt")
