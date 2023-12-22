import camel_cards

data = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""


def test_is_5_of_kind():
    assert camel_cards.is_5_of_kind("AAAAA") is True
    assert camel_cards.is_5_of_kind("33344") is False
    assert camel_cards.is_5_of_kind("5TTTT") is False
