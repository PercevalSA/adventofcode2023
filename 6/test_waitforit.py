import waitforit

input = """Time:      7  15   30
Distance:  9  40  200
"""

def test_parser():
    data = waitforit.parse_input(input)
    assert data[0][0] == 7
    assert data[1] == (15,40)
    assert len(data) == 3
