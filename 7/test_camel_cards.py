import functools

import camel_cards

data = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""


def test_parse():
    parsed = camel_cards.parse_input(data)

    assert parsed[0][0] == "32T3K"
    assert parsed[0][1] == "765"
    assert parsed[-1][0] == "QQQJA"
    assert parsed[-1][1] == "483"
    assert len(parsed) == 5


def test_is_5_of_kind():
    assert camel_cards.is_5_of_kind("AAAAA") is True
    assert camel_cards.is_5_of_kind("33344") is False
    assert camel_cards.is_5_of_kind("5TTTT") is False


def test_is_4_of_kind():
    assert camel_cards.is_4_of_kind("A32AA") is False
    assert camel_cards.is_4_of_kind("A322A") is False
    assert camel_cards.is_4_of_kind("A332A") is False
    assert camel_cards.is_4_of_kind("AAAAA") is True
    assert camel_cards.is_4_of_kind("33343") is True
    assert camel_cards.is_4_of_kind("5TTTT") is True
    assert camel_cards.is_4_of_kind("TTTTA") is True


def test_full_house():
    assert camel_cards.is_full_house("A32AA") is False
    assert camel_cards.is_full_house("A322A") is False
    assert camel_cards.is_full_house("A332A") is False
    assert camel_cards.is_full_house("AAAAA") is True
    assert camel_cards.is_full_house("33343") is False
    assert camel_cards.is_full_house("5TTTT") is False
    assert camel_cards.is_full_house("TTTAA") is True
    assert camel_cards.is_full_house("TTAAT") is True
    assert camel_cards.is_full_house("33444") is True
    assert camel_cards.is_full_house("44334") is True


def test_3_of_kind():
    assert camel_cards.is_3_of_kind("A32AA") is True
    assert camel_cards.is_3_of_kind("A322A") is False
    assert camel_cards.is_3_of_kind("A332A") is False
    assert camel_cards.is_3_of_kind("AAAAA") is False
    assert camel_cards.is_3_of_kind("33343") is False
    assert camel_cards.is_3_of_kind("5TTTT") is False
    assert camel_cards.is_3_of_kind("TTTAA") is True
    assert camel_cards.is_3_of_kind("TTAAT") is True
    assert camel_cards.is_3_of_kind("33444") is True
    assert camel_cards.is_3_of_kind("44334") is True
    assert camel_cards.is_3_of_kind("44534") is True


def test_2_pairs():
    assert camel_cards.is_2_pairs("A32AA") is False
    assert camel_cards.is_2_pairs("A322A") is True
    assert camel_cards.is_2_pairs("A332A") is True
    assert camel_cards.is_2_pairs("AAAAA") is False
    assert camel_cards.is_2_pairs("33343") is False
    assert camel_cards.is_2_pairs("5TTTT") is False
    assert camel_cards.is_2_pairs("TTTAA") is False
    assert camel_cards.is_2_pairs("TTAAT") is False
    assert camel_cards.is_2_pairs("334A4") is True
    assert camel_cards.is_2_pairs("4A334") is True
    assert camel_cards.is_2_pairs("44534") is False


def test_1_pair():
    assert camel_cards.is_1_pair("A32AA") is False
    assert camel_cards.is_1_pair("A322A") is True
    assert camel_cards.is_1_pair("A432A") is True
    assert camel_cards.is_1_pair("AAAAA") is False
    assert camel_cards.is_1_pair("33343") is False
    assert camel_cards.is_1_pair("5TTTT") is False
    assert camel_cards.is_1_pair("T34AA") is True
    assert camel_cards.is_1_pair("TTAAT") is True


def test_high_card():
    assert camel_cards.is_high_card("A322A") is False
    assert camel_cards.is_high_card("AAAAA") is False
    assert camel_cards.is_high_card("33343") is False
    assert camel_cards.is_high_card("T34AA") is False
    assert camel_cards.is_high_card("T234A") is True
    assert camel_cards.is_high_card("23456") is True
    assert camel_cards.is_high_card("4362A") is True


def test_hand_type():
    assert camel_cards.hand_type("A32AA") == 4
    assert camel_cards.hand_type("A322A") == 3
    assert camel_cards.hand_type("A332A") == 3
    assert camel_cards.hand_type("AAAAA") == 7
    assert camel_cards.hand_type("33343") == 6
    assert camel_cards.hand_type("5TTTT") == 6
    assert camel_cards.hand_type("TTTAA") == 5
    assert camel_cards.hand_type("TTAAT") == 5
    assert camel_cards.hand_type("33444") == 5
    assert camel_cards.hand_type("44334") == 5
    assert camel_cards.hand_type("A432A") == 2
    assert camel_cards.hand_type("33343") == 6
    assert camel_cards.hand_type("T34AA") == 2
    assert camel_cards.hand_type("TTAAT") == 5
    assert camel_cards.hand_type("T34AA") == 2
    assert camel_cards.hand_type("T234A") == 1
    assert camel_cards.hand_type("23456") == 1
    assert camel_cards.hand_type("4362A") == 1


def test_compare_same_type_hands():
    assert camel_cards.compare_same_type_hands("A32AA", "A322A") == 1
    assert camel_cards.compare_same_type_hands("TTTAA", "TTAAT") == -1
    assert camel_cards.compare_same_type_hands("TTAAT", "TTTAA") == 1
    assert camel_cards.compare_same_type_hands("T234A", "T234A") == 0
    assert camel_cards.compare_same_type_hands("33444", "44334") == -1
    assert camel_cards.compare_same_type_hands("T234A", "A432A") == -1


def test_compare_hands():
    assert camel_cards.compare_same_type_hands("A32AA", "A322A") == 1
    assert camel_cards.compare_same_type_hands("TTTAA", "TTAAT") == -1
    assert camel_cards.compare_same_type_hands("TTAAT", "TTTAA") == 1
    assert camel_cards.compare_same_type_hands("T234A", "T234A") == 0
    assert camel_cards.compare_same_type_hands("33444", "44334") == -1
    assert camel_cards.compare_same_type_hands("T234A", "A432A") == -1
    assert camel_cards.compare_same_type_hands("A432A", "T234A") == 1
    assert camel_cards.compare_same_type_hands("AAAAA", "33343") == 1
    assert camel_cards.compare_same_type_hands("4362A", "A432A") == -1


def test_compare_bets():
    parsed = camel_cards.parse_input(data)
    parsed.sort(key=functools.cmp_to_key(camel_cards.compare_bets))
    assert parsed[0][0] == "32T3K"
    assert parsed[1][0] == "KTJJT"
    assert parsed[2][0] == "KK677"
    assert parsed[3][0] == "T55J5"
    assert parsed[4][0] == "QQQJA"


def test_calculate_score():
    parsed = camel_cards.parse_input(data)
    parsed.sort(key=functools.cmp_to_key(camel_cards.compare_bets))
    assert camel_cards.calculate_score(parsed) == 6440
