#!/usr/bin/python3
import string
import re

# part 1
def get_calibration(line: str) -> int:
    # replace all letters by none to keep only numbers
    replacement_dict = {ord(i): None for i in string.ascii_lowercase}
    # drop new lines
    num = line.strip('\n').translate(replacement_dict)
    # only keep the first and last number (drop hte numbers in the middle of the string)
    num = num[0] + num[-1]
    return int(num)

def solve_1(data: list[str]) -> int:
    sum = 0
    for line in data:
        sum += get_calibration(line)
    
    return sum

# part 2

numbers_helper = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}
regex = re.compile("|".join(i for i in numbers_helper))

# naïve approach does not solve this case
# eightwothree
# for i, j in numbers_helper.items():
#     line = line.replace(i, str(j))
# maybe regex will treat in order
def words_to_num(line: str) -> str:
    result = ["1"]
    while result:
        result = regex.findall(line) # return a table of matching sub strings
        for substring in result:
            # the replacement is the number with the literal without the forst letter so it does not remove overlayed numbers
            replacement = str(numbers_helper[substring]) + substring[1:]
            # replace only one occurence by one to get numbers in order
            line = line.replace(substring, replacement, 1)

    return line

def solve_2(data: list[str]) -> int:
    sum = 0
    for line in data:
        line = words_to_num(line)
        calib = get_calibration(line)
        sum +=  calib

    return sum


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        data = f.readlines()

    print(f"Regex use to find literal numbers: {regex}")
    print(f"First answer: {solve_1(data)}")
    print(f"Second answer: {solve_2(data)}")