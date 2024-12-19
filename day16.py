from heapq import heappop, heappush
from math import inf

# Read the maze from the input file
with open('data_files/data_day16.txt') as f:
    lines = [line.strip() for line in f]

width, height = len(lines[0]), len(lines)
maze = list("".join(lines))
start_index, end_index = maze.index("S"), maze.index("E")
directions = [-width, 1, width, -1]

visited = dict()
priority_queue = list()
lowest_score = inf
paths = list()

heappush(priority_queue, (0, start_index, 1, ""))  # (score, position, direction, path)
while priority_queue:
    score, position, direction, path = heappop(priority_queue)
    if score > lowest_score:
        break
    if (position, direction) in visited and visited[(position, direction)] < score:
        continue
    visited[(position, direction)] = score
    if position == end_index:
        lowest_score = score
        paths.append(path)
    if maze[position + directions[direction]] != "#":
        heappush(priority_queue, (score + 1, position + directions[direction], direction, path + "F"))
    heappush(priority_queue, (score + 1000, position, (direction + 1) % 4, path + "R"))
    heappush(priority_queue, (score + 1000, position, (direction - 1) % 4, path + "L"))

visited_tiles = set()
visited_tiles.add(start_index)
for path in paths:
    current_position, direction = start_index, 1
    for move in path:
        if move == "L":
            direction = (direction - 1) % 4
        elif move == "R":
            direction = (direction + 1) % 4
        elif move == "F":
            current_position += directions[direction]
            visited_tiles.add(current_position)

print(f"Shortest path: {lowest_score}")
print(f"Optimal viewing positions: {len(visited_tiles)}")