import waitforit

input = """Time:      7  15   30
Distance:  9  40  200
"""

def test_parser():
    data = waitforit.parse_input(input)
    assert data[0][0] == 7
    assert data[1] == (15,40)
    assert len(data) == 3

def test_minimum():
    data = waitforit.parse_input(input)
    assert waitforit.find_minimum_button_time(data[0]) == 2
    assert waitforit.find_minimum_button_time(data[1]) == 4
    assert waitforit.find_minimum_button_time(data[2]) == 11

def test_maximum():
    data = waitforit.parse_input(input)
    assert waitforit.find_maximum_button_time(data[0]) == 5
    assert waitforit.find_maximum_button_time(data[1]) == 11
    assert waitforit.find_maximum_button_time(data[2]) == 19


def test_count_ways_to_solve():
    data = waitforit.parse_input(input)
    assert waitforit.count_ways_to_solve(data[0]) == 4
    assert waitforit.count_ways_to_solve(data[1]) == 8
    assert waitforit.count_ways_to_solve(data[2]) == 9

def test_part_1():
    data = waitforit.parse_input(input)
    assert waitforit.solve_part_1(data) == 288

def test_parsed_data():
    data = waitforit.parse_part_2(input)
    assert data == (71530, 940200)

# 71503 ways
