#!/usr/bin/python3

# for each nuber found extract all surrounding chars and join as a string
# then find symbols in string to detect of it is a part number

# To avoid having to check for borders and hitting them
# we add an extra border of dots around the input

"""
For those using Python, an even easier option is to store the grid in a dict with either (x,y) 
tuples or complex (x+y*1j) coordinates. When querying from the dict, use blah.get(coord, '.') 
and you'll never have an out of bounds concern. Then just iterate over min - 1 to max + 1 for both dimensions.

You can also use collections.defaultdict and a custom function that returns whatever
the desired default value is. In this case you could do something like:

from collections import defaultdict
grid = collections.defaultdict(lambda: '.')
print(grid[20]) # => .

Or whatever you want the default to be.
grid = collections.defaultdict(str)

as str is a function (well, a constructor) that returns an empty string.
"""


# we will store the grid in a dict in order to take advantage of defaultdict
def default_factory(coordinates: tuple) -> str:
    return "."


# LEGACY
def parse_data_as_table(data: str) -> list[list[str]]:
    table = [[letter for letter in line] for line in data.splitlines()]
    return table


def number_length(num_position: int, table: list) -> int:
    length = 0
    while True:
        try:
            int(table[num_position])
            length += 1
            num_position += 1

        except ValueError:
            return length


def extract_surroundings(num_position: int, table: list) -> str:
    return ""


# END LEGACY


def parse_data_as_dict(data: str) -> dict:
    table = {}
    for y, line in enumerate(data.splitlines()):
        for x, letter in enumerate(line):
            table[(x, y)] = letter
    return table


def get_all_num_positions(table: dict) -> list[str]:
    for i in table:
        if table[i].isnumeric():
            yield i


def is_part_number(position: int) -> bool:
    return False


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = f.read()
    plop = parse_data_as_dict(data)
    for i in get_all_num_positions(plop):
        print(i, plop[i])
