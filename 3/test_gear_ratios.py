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


def test_number_length():
    input_1 = [".", ".", ".", ".", "3", "4", "5", ".", ".", "."]
    input_2 = [".", ".", ".", ".", "3", "4", ".", ".", "5", "."]

    assert gear_ratios.number_length(4, input_1) == 3
    assert gear_ratios.number_length(4, input_2) == 2


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
