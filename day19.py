def can_construct(design, patterns):
    if design == "":
        return True
    for pattern in patterns:
        if design.startswith(pattern):
            if can_construct(design[len(pattern):], patterns):
                return True
    return False

def count_ways(design, patterns, memo):
    if design == "":
        return 1
    if design in memo:
        return memo[design]
    
    total_ways = 0
    for pattern in patterns:
        if design.startswith(pattern):
            total_ways += count_ways(design[len(pattern):], patterns, memo)
    
    memo[design] = total_ways
    return total_ways

def main():
    with open('data_files/data_day19.txt') as f:
        lines = f.read().strip().split('\n')
    
    patterns = lines[0].split(', ')
    designs = lines[2:]
    
    part1 = sum(can_construct(design, patterns) for design in designs)
    part2 = sum(count_ways(design, patterns, {}) for design in designs)
    
    print("Part 1, number of possible designs ->", part1)
    print("Part 2, number of ways to make each design ->", part2)

if __name__ == "__main__":
    main()