#!/usr/bin/python3

import haunted_wasteland

data_1 = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
"""

data_2 = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""


def test_parse_node():
    assert haunted_wasteland.parse_node("BBB = (AAA, ZZZ)") == ("BBB", ("AAA", "ZZZ"))


def test_parse():
    parsed = haunted_wasteland.parse_input(data_2)

    assert parsed[0] == "LLR"
    assert parsed[1]["AAA"] == ("BBB", "BBB")
    assert parsed[1]["BBB"] == ("AAA", "ZZZ")
