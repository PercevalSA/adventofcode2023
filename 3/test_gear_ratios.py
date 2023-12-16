import gear_ratios

data = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""


data_reddit = """12.......*..
+.........34
.......-12..
..78........
..*....60...
78.........9
.5.....23..$
8...90*12...
............
2.2......12.
.*.........*
1.1..503+.56"""


def test_parse_data_as_dict():
    parsed_data = gear_ratios.parse_data_as_dict(data)
    assert parsed_data.get((0, 0)) == "4"
    assert parsed_data.get((9, 9)) == "."
    assert parsed_data.get((3, 1)) == "*"


def test_number_len():
    parsed_data = gear_ratios.parse_data_as_dict(data)
    assert gear_ratios.get_number_len((0, 0), parsed_data) == 3
    assert gear_ratios.get_number_len((5, 0), parsed_data) == 3
    assert gear_ratios.get_number_len((2, 2), parsed_data) == 2
    assert gear_ratios.get_number_len((3, 2), parsed_data) == 1
    assert gear_ratios.get_number_len((3, 3), parsed_data) == 0


def test_part_number():
    assert gear_ratios.is_part_number(".") is False
    assert gear_ratios.is_part_number("..") is False
    assert gear_ratios.is_part_number("4") is False
    assert gear_ratios.is_part_number("54") is False
    assert gear_ratios.is_part_number("......5454....5...") is False
    assert gear_ratios.is_part_number(".4...*.5..56...1..2.") is True
    assert gear_ratios.is_part_number(".4...*.5..56...1#..2.") is True
    assert gear_ratios.is_part_number(".4.5445....$") is True


def test_extract_surroundings():
    parsed_data = gear_ratios.parse_data_as_dict(data)
    assert gear_ratios.extract_surroundings((2, 6), 3, parsed_data) == "....+.592......"
    assert gear_ratios.extract_surroundings((3, 8), 1, parsed_data) == "....$.64."


def test_defaultdict():
    parsed_data = gear_ratios.parse_data_as_dict(data)

    assert parsed_data.setdefault((-1, -1), ".") == "."
    assert parsed_data.setdefault((99, 99), ".") == "."
    assert parsed_data.setdefault((10, 10), ".") == "."
    assert parsed_data.setdefault((0, 10), ".") == "."
    assert parsed_data.setdefault((10, 5), ".") == "."

    assert parsed_data.setdefault((0, 0), ".") == "4"
    assert parsed_data.setdefault((9, 9), ".") == "."
    assert parsed_data.setdefault((3, 1), ".") == "*"


def test_get_num_position():
    parsed_data = gear_ratios.parse_data_as_dict(data)
    for i in gear_ratios.get_all_num_positions(parsed_data):
        assert parsed_data.setdefault(i, ".").isnumeric()
        # wrong test we should find all numbers and check is they are returned


def test_get_all_numbers_with_size():
    expected = {
        (0, 0): 3,
        (5, 0): 3,
        (2, 2): 2,
        (6, 2): 3,
        (0, 4): 3,
        (7, 5): 2,
        (2, 6): 3,
        (6, 7): 3,
        (1, 9): 3,
        (5, 9): 3,
    }

    parsed_data = gear_ratios.parse_data_as_dict(data)
    print(expected)
    num_with_size = gear_ratios.get_all_numbers_with_size(parsed_data)
    print(num_with_size)
    assert num_with_size == expected
