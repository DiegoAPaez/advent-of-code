from collections import deque

# Read the input data
with open('data_files/data_day18.txt') as f:
    data = f.read().strip().split('\n')

# Parse the input data into a list of tuples
falling_bytes = [tuple(map(int, line.split(','))) for line in data]

# Initialize the grid
grid_size = 71
grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]

# Define the directions for movement (up, down, left, right)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# BFS to find the shortest path
def bfs(start, end):
    queue = deque([(start, 0)])  # (position, steps)
    visited = set()
    visited.add(start)
    
    while queue:
        (x, y), steps = queue.popleft()
        
        if (x, y) == end:
            return steps
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < grid_size and 0 <= ny < grid_size and grid[ny][nx] == '.' and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), steps + 1))
    
    return -1  # If no path is found

# Part 1: Simulate the first 1024 bytes falling
for x, y in falling_bytes[:1024]:
    grid[y][x] = '#'

# Find the shortest path from (0, 0) to (70, 70)
start = (0, 0)
end = (70, 70)
min_steps = bfs(start, end)

print(f"The minimum number of steps needed to reach the exit is: {min_steps}")

# Part 2: Find the first byte that blocks the path
grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]  # Reset the grid

for i, (x, y) in enumerate(falling_bytes):
    grid[y][x] = '#'
    if bfs(start, end) == -1:
        print(f"The first byte that blocks the path is at: {x},{y}")
        break