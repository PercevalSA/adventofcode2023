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


def are_all_the_same_lst(items: list[str]) -> bool:
    for i in range(len(items) - 1):
        if items[i] != items[i + 1]:
            return False
    return True


def are_all_the_same_str(items: str) -> bool:
    return are_all_the_same_lst(list(items))


def is_5_of_kind(hand: str) -> bool:
    """Five of a kind, where all five cards have the same label: AAAAA"""
    return are_all_the_same_str(hand)


def is_4_of_kind(hand: str) -> bool:
    """Four of a kind, where four cards have the same label
    and one card has a different label: AA8AA
    """
    cards: list[str] = list(hand)
    cards.sort()
    if are_all_the_same_lst(cards[1:-1]) and (
        cards[0] == cards[1] or cards[-1] == cards[-2]
    ):
        return True

    return False


def is_full_house(hand: str) -> bool:
    """Full house, where three cards have the same label,
    and the remaining two cards share a different label: 23332
    """
    cards: list[str] = list(hand)
    cards.sort()

    if (cards[0] == cards[1] == cards[2] and cards[-1] == cards[-2]) or (
        cards[0] == cards[1] and cards[-1] == cards[-2] == cards[-3]
    ):
        return True

    return False


def is_3_of_kind(hand: str) -> bool:
    """Three of a kind, where three cards have the same label,
    and the remaining two cards are each different
    from any other card in the hand: TTT98
    """
    for char in hand:
        if hand.count(char) == 3:
            return True

    return False


def is_2_pairs(hand: str) -> bool:
    """Two pair, where two cards share one label,
    two other cards share a second label,
    and the remaining card has a third label: 23432
    """
    for i in hand:
        if hand.count(i) == 2:
            for j in hand:
                if i != j and hand.count(j) == 2:
                    return True
    return False


def is_1_pair(hand: str) -> bool:
    """One pair, where two cards share one label,
    and the other three cards have a different label
    from the pair and each other: A23A4
    """
    for i in hand:
        if hand.count(i) == 2:
            return True
            # as we tested everything before this is not mandatory
            # hand.replace(i, "")
            # if hand[0] != hand[1] != hand[2]:
            #     return True

    return False


def is_high_card(hand: str) -> bool:
    """High card, where all cards' labels are distinct: 23456"""
    for char in hand:
        if hand.count(char) != 1:
            return False

    return True


def hand_type(hand: str) -> int:
    if is_5_of_kind(hand):
        return 7
    if is_4_of_kind(hand):
        return 6
    if is_full_house(hand):
        return 5
    if is_3_of_kind(hand):
        return 4
    if is_2_pairs(hand):
        return 3
    if is_1_pair(hand):
        return 2
    if is_high_card(hand):
        return 1

    return 0


def parse_input(data: str) -> list:
    lines = data.splitlines()
    return [line.split() for line in lines]


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
