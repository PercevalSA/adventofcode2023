#!/usr/bin/python3

# method
# we need to parse the graph which seems the most complicated part
# then apply a shorter path algorithm which would be dijkstra. We can use a std lib algo
# or implement it ourselves. I will implement it myself for the fun of it and the sweet
# sweet memories of telecom algo classes

# all nodes will be represented with their x,y position in the maze as a tuple of int
# the maze will be a dict which is faster to search in than a list

# to analyse connexions we need to determine orientations of the pipes, we will associates
# orientations to a pipe symbole then determine if other symbols around are compatibles
orientations = {"N", "E", "S", "W"}
compatibilities = {
    "-": [],
    "|": [],
    "7": ["E", "S"],
    "F": [],
    "J": [],
    "L": [],
}


def get_edges(node: tuple[int, int]) -> list[tuple[int, int]]:
    """Return the edges of a given node"""
    return []


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
