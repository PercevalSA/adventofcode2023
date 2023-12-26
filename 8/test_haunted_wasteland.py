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


def test_iterate_instructions():
    instructions, map = haunted_wasteland.parse_input(data_1)
    assert haunted_wasteland.iterate_instructions(instructions, map, "AAA", "ZZZ") == 2

    instructions, map = haunted_wasteland.parse_input(data_2)
    assert haunted_wasteland.iterate_instructions(instructions, map, "AAA", "ZZZ") == 6


data_part_2 = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""


def test_solve_part_2():
    assert haunted_wasteland.solve_part_2(data_part_2) == 6
