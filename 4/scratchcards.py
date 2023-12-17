#!/usr/bin/python3


def parse_data(data: str) -> list:
    result = []
    for line in data.splitlines():
        winning_numbers_str, numnbers_str = line.split(":")[1].split("|")
        winning_numbers = [int(i) for i in winning_numbers_str.strip().split()]
        numbers = [int(i) for i in numnbers_str.strip().split()]

        result.append([winning_numbers, numbers])

    return result


def count_wins(card: list[list]) -> int:
    wins = 0
    for number in card[1]:
        if number in card[0]:
            wins += 1

    return wins


def card_score(wins: int) -> int:
    if wins >= 2:
        return 2 ** (wins - 1)
    else:
        return wins


def solve_part_1(data: list):
    score = 0
    for card in data:
        score += card_score(count_wins(card))

    return score


# part 2
def get_winned_cards(card: list, index: int, max_id: int) -> list[int]:
    wins = count_wins(card)
    return [index + i for i in range(1, wins + 1) if index + i <= max_id]


def generate_originals_and_copies_indexes(data: list) -> list[int]:
    # generates the list of all cards: original + copy to be processeced after
    # we only generates indexes to spare memory
    max = len(data)
    all_cards_indexes: list[int] = [i for i in range(max)]
    for index in all_cards_indexes:
        for win in get_winned_cards(data[index], index, max):
            all_cards_indexes.append(win)

    return all_cards_indexes


def solve_part_2(data: list) -> int:
    # how many total scratchcards do you end up with?
    return len(generate_originals_and_copies_indexes(data))


def main(file: str):
    with open(file, "r") as f:
        data = f.read()
    parsed_data = parse_data(data)

    result = solve_part_1(parsed_data)
    print(f"Result 1: {result}")

    result = solve_part_2(parsed_data)
    print(f"Result 2: {result}")


if __name__ == "__main__":
    main("4/input.txt")
