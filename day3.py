import re

# Regular expressions to find valid mul instructions and commands
MUL_RE = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
COMMAND_RE = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)")

# Read the file contents
file_path = 'data_files/data_day3.txt'  # Path to the uploaded file
with open(file_path, 'r') as file:
    RAW = file.read()  # Read the entire file content into RAW

# Part 1: Sum of all valid mul(X, Y) instructions
def part_one():
    total = 0
    for match in MUL_RE.finditer(RAW):
        a, b = match.groups()
        total += int(a) * int(b)
    return total

# Part 2: Sum of mul(X, Y) instructions with do()/don't() toggles
def part_two():
    enabled = True
    total = 0
    for match in COMMAND_RE.finditer(RAW):
        if match[0] == "do()":
            enabled = True
        elif match[0] == "don't()":
            enabled = False
        elif enabled:
            a, b = match.groups()
            total += int(a) * int(b)
    return total

# Submit the solutions for both parts (assuming aoc_lube is available in the context)
print("Part 1 result:", part_one())
print("Part 2 result:", part_two())