import numpy as np

# for each nuber found extract all surrounding chars and join as a string
# then find symbols in string to detect of it is a part number

# To avoid having to check for borders and hitting them
# we add an extra border of dots around the input

"""
For those using Python, an even easier option is to store the grid in a dict with either (x,y) tuples or complex (x+y*1j) coordinates. When querying from the dict, use blah.get(coord, '.') and you'll never have an out of bounds concern. Then just iterate over min - 1 to max + 1 for both dimensions.
7
User avatar
level 2
rabuf
·
9 days ago

You can also use collections.defaultdict and a custom function that returns whatever the desired default value is. In this case you could do something like:

from collections import defaultdict
grid = collections.defaultdict(lambda: '.')
print(grid[20]) # => .

Or whatever you want the default to be.
3
User avatar
level 3
Anceps2
·
9 days ago

You can write:

grid = collections.defaultdict(str)

as str is a function (well, a constructor) that returns an empty string.
"""


def is_part_number(position: int) -> bool:
    return False


def parse_data(data: str) -> np.matrix:
    table = [[letter for letter in line] for line in data.splitlines()]
    return np.matrix(table)


def number_length(num_position: int, table: np.matrix) -> int:
    length = 0
    while True:
        try:
            int(table[num_position])
            length += 1
            num_position += 1

        except ValueError:
            return length


def extract_surroundings(num_position: int, table: np.matrix) -> str:
    return ""


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = f.read()
    print(parse_data(data))
