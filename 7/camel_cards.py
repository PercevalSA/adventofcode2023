#!/usr/bin/python3

strength_order = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "J": 10,
    "T": 9,
    "9": 8,
    "8": 7,
    "7": 6,
    "6": 5,
    "5": 4,
    "4": 3,
    "3": 2,
    "2": 1,
}


def is_5_of_kind(hand: str) -> bool:
    """Five of a kind, where all five cards have the same label: AAAAA"""
    cards = list(hand)
    for i in range(len(cards) - 1):
        if cards[i] != cards[i + 1]:
            return False
    return True


def is_4_of_kind(hand: str) -> bool:
    """Four of a kind, where four cards have the same label
    and one card has a different label: AA8AA
    """
    return False


def is_full_house(hand: str) -> bool:
    """Full house, where three cards have the same label,
    and the remaining two cards share a different label: 23332
    """
    return False


def is_3_of_kind(hand: str) -> bool:
    """Three of a kind, where three cards have the same label,
    and the remaining two cards are each different
    from any other card in the hand: TTT98
    """
    return False


def is_2_pairs(hand: str) -> bool:
    """Two pair, where two cards share one label,
    two other cards share a second label,
    and the remaining card has a third label: 23432
    """
    return False


def is_1_pair(hand: str) -> bool:
    """One pair, where two cards share one label,
    and the other three cards have a different label
    from the pair and each other: A23A4
    """
    return False


def is_high_card(hand: str) -> bool:
    """High card, where all cards' labels are distinct: 23456"""
    return False


def parse_input(data: str) -> list:
    return data.splitlines()


def solve_part_1(data: list):
    return 0


def main(file: str):
    with open(file, "r") as f:
        data = f.read()

    parsed_data = parse_input(data)
    result = solve_part_1(parsed_data)
    print(f"Result 1: {result}")


if __name__ == "__main__":
    main("7/input.txt")
