#!/usr/bin/python3

"""
Determine which games would have been possible if the bag had been loaded with only
12 red cubes
13 green cubes
14 blue cubes
What is the sum of the IDs of those games?
"""


def parse_draw(data: str) -> dict:
    draw = {}
    cubes = data.split(",")
    for cube in cubes:
        color = cube.strip().split(" ")
        draw[color[1]] = int(color[0])

    # sort dict by alphabetical order of colors
    # return dict(sorted(draw.items()))
    return draw


def parse_input(data: list[str]) -> dict:
    games: dict = {}
    for line in data:
        game_number, line = line.split(":")

        draws: dict = {}
        for id, draw in enumerate(line.split(";")):
            draws[id] = parse_draw(draw)

        games[game_number] = draws

    print(games)
    return games


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = f.readlines()

    games = parse_input(data)
