#!/usr/bin/python3

def parse_input(data: str) -> list[tuple[int, int]]:
    times, distances = [line.split()[1:] for line in data.splitlines()]
    return [(int(t), int(d)) for t, d in zip(times, distances)]


def distance_from_button_pressed_time(button_time: int, total_time: int) -> int:
    sailing_time = total_time - button_time
    sailed_distance = sailing_time * button_time # button time is speed
    return sailed_distance


# we assume that the results are somehow gaussian
def find_button_time(total_time: int, distance_to_beat: int):
    for i in range(total_time):
        if distance_from_button_pressed_time(i, total_time) > distance_to_beat:
            return i

def find_minimum_button_time(race: tuple[int, int]):
    find_button_time(race[0], race[1])

# one full millisecond hold = one millimeter per millisecond
def main(file: str):
    with open(file, "r") as f:
        data = f.read()

    result = None
    print(f"Result 1: {result}")


if __name__ == "__main__":
    main("6/input.txt")
