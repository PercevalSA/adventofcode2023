import cube_conundrum


def test_parse_draw():
    input = "3 green, 3 red, 4 blue"
    expected = {"blue": 4, "green": 3, "red": 3}

    assert expected == cube_conundrum.parse_draw(input)


def test_parse_game():
    input = ["Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"]
    expected = {
        "Game 4": {
            0: {"blue": 6, "green": 1, "red": 3},
            1: {"green": 3, "red": 6},
            2: {"blue": 15, "green": 3, "red": 14},
        }
    }

    assert expected == cube_conundrum.parse_input(input)


def test_is_possible():
    input = {"blue": 10, "green": 9, "red": 8}
    assert cube_conundrum.is_possible(input)


def test_is_possible_limit():
    input = {"blue": 14, "green": 13, "red": 12}
    assert cube_conundrum.is_possible(input)


def test_is_possible_impossible():
    input = {"blue": 20, "green": 21, "red": 102}
    assert cube_conundrum.is_possible(input) is False

    input_2 = {"blue": 2, "green": 21, "red": 10}
    assert cube_conundrum.is_possible(input_2) is False
