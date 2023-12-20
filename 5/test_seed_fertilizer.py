import seed_fertilizer

data = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

"""
Seed 79, soil 81, fertilizer 81, water 81, light 74, temperature 78, humidity 78, location 82.
Seed 14, soil 14, fertilizer 53, water 49, light 42, temperature 42, humidity 43, location 43.
Seed 55, soil 57, fertilizer 57, water 53, light 46, temperature 82, humidity 82, location 86.
Seed 13, soil 13, fertilizer 52, water 41, light 34, temperature 34, humidity 35, location 35.
"""
expected = [82, 43, 86, 35]


def test_parse_data():
    sf = seed_fertilizer.FieldAnalyzer(data)
    assert sf.data["seed-to-soil"][98] == 50
    assert sf.data["seed-to-soil"][99] == 51
    assert sf.data["seed-to-soil"][50] == 52
    assert sf.data["seed-to-soil"][100] == 100

    assert sf.data["fertilizer-to-water"][53] == 49
    assert sf.data["fertilizer-to-water"][60] == 56
    assert sf.data["fertilizer-to-water"][11] == 0
    assert sf.data["fertilizer-to-water"][52] == 41


def test_resolver():
    sf = seed_fertilizer.FieldAnalyzer(data)

    assert sf.resolver("fertilizer-to-water", 53) == 49
    assert sf.resolver("fertilizer-to-water", 60) == 56
    assert sf.resolver("fertilizer-to-water", 11) == 0
    assert sf.resolver("fertilizer-to-water", 52) == 41

    assert sf.resolver("fertilizer-to-water", 53) == 49
    assert sf.resolver("fertilizer-to-water", 60) == 56
    assert sf.resolver("fertilizer-to-water", 11) == 0
    assert sf.resolver("fertilizer-to-water", 52) == 41


def test_find_location():
    sf = seed_fertilizer.FieldAnalyzer(data)
    result = sf.seed_to_location()
    for i, j in zip(result, expected):
        assert i == j
