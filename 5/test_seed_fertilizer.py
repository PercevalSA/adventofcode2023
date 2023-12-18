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

def test_parse_data():
    sf = seed_fertilizer.FieldAnalyzer(data)
    print(sf.data)
    assert sf.data["seed-to-soil"][98] == 50
    assert sf.data["seed-to-soil"][99] == 51
    assert sf.data["seed-to-soil"][50] == 52
    assert sf.data["seed-to-soil"][100] == 100

    assert sf.data["fertilizer-to-water"][53] == 49
    assert sf.data["fertilizer-to-water"][60] == 56
    assert sf.data["fertilizer-to-water"][11] == 0
    assert sf.data["fertilizer-to-water"][52] == 41




