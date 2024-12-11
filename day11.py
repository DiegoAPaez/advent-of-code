from functools import lru_cache

def read_input(file_path):
    with open(file_path, 'r') as file:
        return list(map(int, file.read().strip().split()))

@lru_cache(None)
def blink(stone, n):
    if n == 0:
        return 1

    n -= 1
    if stone == 0:
        return blink(1, n)

    m, r = divmod(len(str(stone)), 2)
    if r == 0:
        a, b = divmod(stone, 10**m)
        return blink(a, n) + blink(b, n)

    return blink(stone * 2024, n)

def solve_part1(file_path):
    stones = read_input(file_path)
    return sum(blink(stone, 25) for stone in stones)

def solve_part2(file_path):
    stones = read_input(file_path)
    return sum(blink(stone, 75) for stone in stones)

if __name__ == '__main__':
    file_path = 'data_files/data_day11.txt'
    print(f"Part 1: {solve_part1(file_path)}")
    print(f"Part 2: {solve_part2(file_path)}")