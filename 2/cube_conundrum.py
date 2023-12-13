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
        games[game_number] = [parse_draw(draw) for draw in line.split(";")]

    print(games)
    return games


def draw_is_possible(draw: dict) -> bool:
    maximum = {"blue": 14, "green": 13, "red": 12}

    for color in draw:
        if draw[color] > maximum[color]:
            return False

    return True


def game_is_possible(game: dict) -> bool:
    for draw in game:
        if draw_is_possible(draw) is False:
            return False

    return True


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = f.readlines()

    games = parse_input(data)
    for game in games:
        print(game, game_is_possible(games[game]))

    # we need to check if all draws in a game are possible
