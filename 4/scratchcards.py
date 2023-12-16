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


def solve_part_1(data: list):
    return data


def main(file: str):
    with open(file, "r") as f:
        data = f.read()
    parsed_data = parse_data(data)

    result = solve_part_1(parsed_data)
    print(f"Result 1: {result}")


if __name__ == "__main__":
    main("4/input.txt")
