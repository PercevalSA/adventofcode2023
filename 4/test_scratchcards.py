#!/usr/bin/python3

import scratchcards

input = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""


wins = [4, 2, 2, 1, 0, 0]
scores = [2, 2, 1, 0, 0]


def test_parse_data():
    expected = [[41, 48, 83, 86, 17], [83, 86, 6, 31, 17, 9, 48, 53]]
    result = scratchcards.parse_data(input)

    assert result[0] == expected


def test_count_wins():
    parsed_data = scratchcards.parse_data(input)
    for line, win in zip(parsed_data, wins):
        assert scratchcards.count_wins(line) == win


def test_scores():
    assert scratchcards.card_score(0) == 0
    assert scratchcards.card_score(1) == 1
    assert scratchcards.card_score(2) == 2
    assert scratchcards.card_score(3) == 4
    assert scratchcards.card_score(4) == 8
    assert scratchcards.card_score(5) == 16


def test_get_winned_cards():
    parsed_data = scratchcards.parse_data(input)
    print(parsed_data)
    # Card 1 has four matching numbers,
    # so you win one copy each of the next four cards: cards 2, 3, 4, and 5.
    assert scratchcards.get_winned_cards(parsed_data[0], 0, len(parsed_data)) == [
        1,
        2,
        3,
        4,
    ]
    assert scratchcards.get_winned_cards(parsed_data[0], 0, 3) == [1, 2, 3]
    assert scratchcards.get_winned_cards(parsed_data[1], 1, len(parsed_data)) == [2, 3]
    assert scratchcards.get_winned_cards(parsed_data[5], 5, len(parsed_data)) == []
    assert scratchcards.get_winned_cards(parsed_data[4], 4, len(parsed_data)) == []
