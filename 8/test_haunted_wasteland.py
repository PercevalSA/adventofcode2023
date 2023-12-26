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

    assert parsed[0] == "AAA"
    assert parsed[1] == "LLR"
    assert parsed[2]["AAA"] == ("BBB", "BBB")
    assert parsed[2]["BBB"] == ("AAA", "ZZZ")


def test_iterate_instructions():
    start, instructions, map = haunted_wasteland.parse_input(data_2)

    result = haunted_wasteland.iterate_instructions(instructions, map, start, "ZZZ")
    assert result == 6