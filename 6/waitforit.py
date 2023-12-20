#!/usr/bin/python3

def parse_input(data: str) -> list[tuple[int, int]]:
    times, distances = [line.split()[1:] for line in data.splitlines()]
    return [(int(t), int(d)) for t, d in zip(times, distances)]

def parse_part_2(data: str) -> tuple[int,int]:
    time, distance = ["".join(line.split()[1:]) for line in data.splitlines()]
    return (int(time), int(distance))

def distance_from_button_pressed_time(button_time: int, total_time: int) -> int:
    sailing_time = total_time - button_time
    sailed_distance = sailing_time * button_time # button time is speed
    return sailed_distance


def find_minimum_button_time(race: tuple) -> int:
    total_time, distance_to_beat = race
    for i in range(total_time):
        if distance_from_button_pressed_time(i, total_time) > distance_to_beat:
            return i


def find_maximum_button_time(race: tuple) -> int:
    total_time, distance_to_beat = race
    for i in reversed(range(total_time)):
        if distance_from_button_pressed_time(i, total_time) > distance_to_beat:
            return i


def count_ways_to_solve(race: tuple) -> int:
    return find_maximum_button_time(race) - find_minimum_button_time(race) + 1


def solve_part_1(data: list):
    result = 1
    for race in data:
        result = result * count_ways_to_solve(race)
    return result

def solve_part_2(data: tuple):
    return count_ways_to_solve(data)


# one full millisecond hold = one millimeter per millisecond
def main(file: str):
    with open(file, "r") as f:
        data = f.read()

    parsed_data = parse_input(data)
    result = solve_part_1(parsed_data)
    print(f"Result 1: {result}")

    parsed_data = parse_part_2(data)
    result = solve_part_2(parsed_data)
    print(f"Result 2: {result}")


if __name__ == "__main__":
    main("6/input.txt")
