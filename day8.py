import numpy as np
from itertools import combinations

def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    return lines

def parse_grid(lines):
    return np.array([list(line) for line in lines])

def inbounds(y, x, H, W):
    return 0 <= y < H and 0 <= x < W

def mark_podes(y, x, dy, dx, podes, H, W, part):
    if part == 1:
        if inbounds(y + dy, x + dx, H, W):
            podes[y + dy, x + dx] = 1
        return

    while inbounds(y, x, H, W):
        podes[y, x] = 1
        y += dy
        x += dx

def sum_antipodes(grid, part):
    H, W = grid.shape
    antipodes = np.zeros((H, W), int)
    frequencies = [freq for freq in np.unique(grid) if freq != '.']
    for freq in frequencies:
        for a, b in combinations(np.argwhere(grid == freq), r=2):
            mark_podes(*a, *a - b, antipodes, H, W, part)
            mark_podes(*b, *b - a, antipodes, H, W, part)
    return antipodes.sum()

def count_unique_antinode_positions(file_path, part):
    lines = read_input(file_path)
    grid = parse_grid(lines)
    return sum_antipodes(grid, part)

# Example usage:
file_path = 'data_files/data_day8.txt'
print("Part 1 result:", count_unique_antinode_positions(file_path, 1))
print("Part 2 result:", count_unique_antinode_positions(file_path, 2))