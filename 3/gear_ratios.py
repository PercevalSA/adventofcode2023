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


def parse_data_as_dict(data: str) -> dict:
    table = {}
    for y, line in enumerate(data.splitlines()):
        for x, letter in enumerate(line):
            table[(x, y)] = letter
    return table


def get_all_num_positions(table: dict) -> tuple:
    for i in table:
        if table[i].isnumeric():
            yield i


def get_number_len(position: tuple[int, int], table: dict) -> int:
    len = 0
    # iterate on the line and check if the char is int, increase len
    # if we find something else return the len because the nulmber has ended
    while table.setdefault((position[0] + len, position[1]), ".").isnumeric():
        len += 1
    return len


def get_all_numbers_with_size(table: dict) -> dict[tuple[int, int], int]:
    plop = {}
    all_nums = iter(get_all_num_positions(table))
    for num in all_nums:
        size = get_number_len(num, table)
        print(num, table.get(num), size)
        for _ in range(1, size):
            next(all_nums)
        plop[num] = size

    return plop


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


if __name__ == "__main__":
    with open("3/input.txt", "r") as f:
        data = f.read()
    plop = parse_data_as_dict(data)
    for i in get_all_num_positions(plop):
        print(i, plop[i])
