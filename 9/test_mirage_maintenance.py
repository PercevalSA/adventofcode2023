#!/usr/bin/python3

import mirage_maintenance

data = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

solutions = [18, 28, 68]


def test_parse():
    parsed = mirage_maintenance.parse_data(data)
    assert parsed[0][0] == 0
    assert parsed[0][5] == 15
    assert parsed[2][2] == 16
    assert parsed[2][5] == 45


def test_get_steps():
    assert mirage_maintenance.get_steps([0, 3, 6, 9, 12, 15]) == [3, 3, 3, 3, 3]


def test_solve_part_1():
    assert mirage_maintenance.solve_part_1(data) == 114
