import trebuchet

data_1 = {
    "1abc2": 12,
    "pqr3stu8vwx": 38,
    "a1b2c3d4e5f": 15,
    "treb7uchet": 77,
}

data_2 = {
    "two1nine": 29,
    "eightwothree": 83,
    "abcone2threexyz": 13,
    "xtwone3four": 24,
    "4nineeightseven2": 42,
    "zoneight234": 14,
    "7pqrstsixteen": 76,
}

def test_get_calibration():
    for input, expected, in data_1.items():
        assert trebuchet.get_calibration(input) == expected

def test_solution_1():
    expected = sum(data_1.values())
    assert trebuchet.solve_1(data_1.keys()) == expected
