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


def test_generate_originals_and_copies_indexes():
    """
    Card 1 has four matching numbers, so you win one copy each of the next four cards: cards 2, 3, 4, and 5.
    Your original card 2 has two matching numbers, so you win one copy each of cards 3 and 4.
    Your copy of card 2 also wins one copy each of cards 3 and 4.
    Your four instances of card 3 (one original and three copies) have two matching numbers, so you win four copies each of cards 4 and 5.
    Your eight instances of card 4 (one original and seven copies) have one matching number, so you win eight copies of card 5.
    Your fourteen instances of card 5 (one original and thirteen copies) have no matching numbers and win no more cards.
    Your one instance of card 6 (one original) has no matching numbers and wins no more cards.
    """

    parsed_data = scratchcards.parse_data(input)
    result = scratchcards.generate_originals_and_copies_indexes(parsed_data)

    # you end up with 1 instance of card 1,
    assert result.count(0) == 1
    # 2 instances of card 2,
    assert result.count(1) == 2
    # 4 instances of card 3,
    assert result.count(2) == 4
    # 8 instances of card 4,
    assert result.count(3) == 8
    # 14 instances of card 5,
    assert result.count(4) == 14
    # 1 instance of card 6.
    assert result.count(5) == 1
    # In total, this example pile of scratchcards causes you to ultimately have 30
    assert len(result) == 30
