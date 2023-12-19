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
