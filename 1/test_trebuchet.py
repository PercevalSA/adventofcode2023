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

data_3 = {
    "two1nine": "2wo19ine",
    "eightwothree": "8igh2wo3hree",
    "abcone2threexyz": "abc1ne23hreexyz",
    "xtwone3four": "x2w1ne34our",
    "4nineeightseven2": "49ine8ight7even2",
    "zoneight234": "z1n8ight234",
    "7pqrstsixteen": "7pqrst6ixteen",
}

data_reddit = {"eighthree": 83, "sevenine": 79, "oneight": 18}
data_reddit_2 = {"eighthree": "8igh3hree", "sevenine": "7eve9ine", "oneight": "1n8ight"}


def test_get_calibration():
    for input, expected, in data_1.items():
        assert expected == trebuchet.get_calibration(input)

def test_solution_1():
    expected = sum(data_1.values())
    assert expected == trebuchet.solve_1(data_1.keys())

def test_words_to_num():
    for input, expected in data_3.items():
        assert expected == trebuchet.words_to_num(input)

def test_get_calibration_2():
    for key in data_2.keys():
        print(key)
        input = data_3[key]
        expected = data_2[key]
        assert expected == trebuchet.get_calibration(input) 

def test_solution_2():
    expected = sum(data_2.values())
    assert expected == trebuchet.solve_2(data_2.keys())

# source: https://www.reddit.com/r/adventofcode/comments/1884fpl/2023_day_1for_those_who_stuck_on_part_2/
def test_words_to_num_extra():

    for input, expected in data_reddit_2.items():
        result = trebuchet.words_to_num(input)
        assert expected == result

def test_solution_2_extra():
    expected = sum(data_reddit.values())
    assert expected == trebuchet.solve_2(data_reddit.keys())