import cube_conundrum

data = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

minimum_cubes_needed = {
    "Game 1": {"blue": 6, "green": 2, "red": 4},
    "Game 2": {"blue": 4, "green": 3, "red": 1},
    "Game 3": {"blue": 6, "green": 13, "red": 20},
    "Game 4": {"blue": 15, "green": 3, "red": 14},
    "Game 5": {"blue": 2, "green": 3, "red": 6},
}

powers = {"Game 1": 48, "Game 2": 12, "Game 3": 1560, "Game 4": 630, "Game 5": 36}

def test_parse_draw():
    input = "3 green, 3 red, 4 blue"
    expected = {"blue": 4, "green": 3, "red": 3}

    assert expected == cube_conundrum.parse_draw(input)


def test_parse_game():
    input = ["Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"]
    expected = {
        "Game 4": [
            {"blue": 6, "green": 1, "red": 3},
            {"green": 3, "red": 6},
            {"blue": 15, "green": 3, "red": 14},
        ]
    }

    assert expected == cube_conundrum.parse_input(input)


def test_is_possible():
    input = {"blue": 10, "green": 9, "red": 8}
    assert cube_conundrum.draw_is_possible(input) is True

    input = {"blue": 7, "green": 3}
    assert cube_conundrum.draw_is_possible(input) is True


def test_is_possible_limit():
    input = {"blue": 14, "green": 13, "red": 12}
    assert cube_conundrum.draw_is_possible(input) is True


def test_is_possible_impossible():
    input = {"blue": 20, "green": 21, "red": 102}
    assert cube_conundrum.draw_is_possible(input) is False

    input_2 = {"blue": 2, "green": 21, "red": 10}
    assert cube_conundrum.draw_is_possible(input_2) is False

    input_2 = {"green": 21, "red": 10}
    assert cube_conundrum.draw_is_possible(input_2) is False


def test_minimum_cubes_needed():
    games = cube_conundrum.parse_input(data.split("\n"))
    for game in games:
        assert cube_conundrum.minimum_cubes_needed(games[game]) == minimum_cubes_needed[game]


def test_get_cube_power():
    assert 36 == cube_conundrum.get_cube_power({"blue": 4, "green": 3, "red": 3})
    assert 1 == cube_conundrum.get_cube_power({"blue": 1, "green": 1, "red": 1})
    assert 3 == cube_conundrum.get_cube_power({"blue": 1, "green": 3})
    assert 8 == cube_conundrum.get_cube_power({"green": 4, "red": 2})

def test_get_cube_power_2():
    games = cube_conundrum.parse_input(data.split("\n"))

    for game in games:
        assert powers[game] == cube_conundrum.get_cube_power(cube_conundrum.minimum_cubes_needed(games[game]))