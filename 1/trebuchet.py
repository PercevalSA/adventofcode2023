#!/usr/bin/python3
import string
import re

with open('input.txt', 'r') as f:
    data = f.readlines()

# part 1
def get_calibration(line: str) -> int:
    # replace all letters by none to keep only numbers
    replacement_dict = {ord(i): None for i in string.ascii_lowercase}
    # drop new lines
    num = line.strip('\n').translate(replacement_dict)
    # only keep the first and last number (drop hte numbers in the middle of the string)
    num = num[0] + num[-1]
    return int(num)

def solve_1():
    sum = 0
    for line in data:
        sum += get_calibration(line)
    print(f"First answer: {sum}")

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

# naïve approach does not solve this case
# eightwothree
# for i, j in numbers_helper.items():
#     line = line.replace(i, str(j))
# maybe regex will treat in order

regex = re.compile("|".join(i for i in numbers_helper))
print(f"Regex use to find literal numbers: {regex}")

def solve_2():
    sum = 0
    for line in data:
        result = regex.findall(line) # return a table of matching sub strings
        for substring in result:
            # replace only one occurence by one to get numbers in order
            line = line.replace(substring, str(numbers_helper[substring]), 1)

        sum += get_calibration(line)

    print(f"Second answer: {sum}")


if __name__ == "__main__":
    solve_1()
    solve_2()