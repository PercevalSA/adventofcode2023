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

    waitforit.find_minimum_button_time(data[0]) == 5
    waitforit.find_minimum_button_time(data[1]) == 4
    waitforit.find_minimum_button_time(data[2]) == 11
