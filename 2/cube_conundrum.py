#!/usr/bin/python3

import functools
import operator

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


def get_game_number(game: str) -> int:
    # parse "Game 43"
    return int(game.split(" ")[-1])


def minimum_cubes_needed(game: dict) -> dict:
    """ find the maximum of cube per color for a given game, 
    that's the minimum of cubes needed
    """
    maximum = {"blue": 0, "green": 0, "red": 0}

    for draw in game:
        for color in draw:
            if draw[color] > maximum[color]:
                maximum[color] = draw[color]
    
    return maximum

def get_cube_power(draw: dict) -> int:
    """ return the number of cubes in a draw """
    return functools.reduce(operator.mul, draw.values(), 1)

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = f.readlines()
    games = parse_input(data)

    # step 1
    result = 0
    for game in games:
        if game_is_possible(games[game]):
            result += get_game_number(game)

    print(f"Result 1: {result}")
    # we need to check if all draws in a game are possible

    # step 2
    power = 0
    for game in games:
        power += get_cube_power(minimum_cubes_needed(games[game]))

    print(f"Result 2: {power}")
