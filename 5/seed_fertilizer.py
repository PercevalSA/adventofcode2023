#!/usr/bin/python3

from collections import defaultdict 


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
            block_content = block_content.strip().split()
        else:
            block_content = self._parse_numbers(block_content.strip())

        print("block", block_name, block_content)
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


    def solve_part_1(self) -> int:
        return 0

def main(file: str):
    with open(file, "r") as f:
        data = f.read()

    filed_analyzer = FieldAnalyzer(data)

    result = filed_analyzer.solve_part_1()
    print(f"Result 1: {result}")


if __name__ == "__main__":
    main("5/input.txt")
