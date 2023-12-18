#!/usr/bin/python3

# we can use defaultdict to generat missing part as it is only int to int correspondances
# default dict does not take any argument to generate missing parts we need our own dict type
# we need to develop a resolver instead to solve the problem in an acceptable time
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

    def resolver(self, table_name: str, number: int):
        for case in self._data[table_name]:
            src = case[0]
            dst = case[1]
            ran = case[2]
            if src <= number <= src + ran:
                diff = number - src
                return dst + diff

        return number

    def _parse_numbers(self, table: str) -> list[tuple]:
        correspondance = []
        for line in table.split("\n"):
            dest, src, ran = line.split()
            correspondance.append((int(src), int(dest), int(ran)))

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
            location = self.resolver(
                "humidity-to-location",
                self.resolver(
                    "temperature-to-humidity",
                    self.resolver(
                        "light-to-temperature",
                        self.resolver(
                            "water-to-light",
                            self.resolver(
                                "fertilizer-to-water",
                                self.resolver(
                                    "soil-to-fertilizer",
                                    self.resolver("seed-to-soil", s),
                                ),
                            ),
                        ),
                    ),
                ),
            )
            result.append(location)
        return result


def main(file: str):
    with open(file, "r") as f:
        data = f.read()

    field_analyzer = FieldAnalyzer(data)
    locations = field_analyzer.seed_to_location()
    print(locations)
    result = min(locations)

    print(f"Result 1: {result}")


if __name__ == "__main__":
    main("5/input.txt")
