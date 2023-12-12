#!/usr/bin/python3
import string
 
with open('input.txt', 'r') as f:
    data = f.readlines()

sum = 0
for i in data:
    # replace all letters by none to keep only numbers
    replacement_dict = {ord(i): None for i in string.ascii_lowercase}
    # drop new lines
    num = i.strip('\n').translate(replacement_dict)
    # only keep the first and last number (drop hte numbers in the middle of the string)
    num = num[0] + num[-1]
    sum += int(num)

print(f"First answer: {sum}")