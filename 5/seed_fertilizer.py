#!/usr/bin/python3

# we can use defaultdict to generat missing part as it is only int to int correspondances
# default dict does not take any argument to generate missing parts we need our own dict type
class MyDict(dict):
    __missing__ = lambda self, key: key

class FieldAnalyzer:
    def __init__(self, data_src: str):
        self._data_src = data_src
        self._data = self._parse_data(self._data_src)
    
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @data.deleter
    def data(self):
        del self._data


    def _parse_numbers(self, table: str) -> dict[int, int]:
        correspondance = MyDict()
        for line in table.split('\n'):
            dest, src, ran = line.split()
            for i in range(int(ran)):
                correspondance[int(src) + i] = int(dest) + i

        return correspondance

    def _parse_block(self, block: str) -> tuple:
        block_name, block_content = block.split(":")
        if block_name == "seeds":
            block_content = [int(i) for i in block_content.strip().split()]
        else:
            block_content = self._parse_numbers(block_content.strip())

        # print("block", block_name, block_content)
        return block_name.split()[0], block_content

    def _parse_data(self, data: str) -> dict:
        """each block is seperated by a line gap, then a title followed by:
        finally all numbers are parsed the same way"""
        parsed_data = {}
        # split by block before parsing each data
        for block in data.split("\n\n"):
            data_name, data_content = self._parse_block(block)
            parsed_data[data_name] = data_content

        return parsed_data


    def seed_to_location(self) -> list[int]:
        result = []
        for s in self._data["seeds"]:
            location = self._data["humidity-to-location"][self._data["temperature-to-humidity"][self._data["light-to-temperature"][self._data["water-to-light"][self._data["fertilizer-to-water"][self._data["soil-to-fertilizer"][self._data["seed-to-soil"][s]]]]]]]
            result.append(location)
        return result


def main(file: str):
    with open(file, "r") as f:
        data = f.read()

    field_analyzer = FieldAnalyzer(data)
    locations = field_analyzer.seed_to_location()
    result = min(locations)

    print(f"Result 1: {result}")


if __name__ == "__main__":
    main("5/input.txt")
