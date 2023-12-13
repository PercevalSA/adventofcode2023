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
