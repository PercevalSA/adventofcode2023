import cube_conundrum

data = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""


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
