import networkx as nx

def read_input(file_path):
    with open(file_path, 'r') as file:
        return [list(map(int, line.strip())) for line in file]

def find_trailheads(map_data):
    trailheads = []
    for i, row in enumerate(map_data):
        for j, height in enumerate(row):
            if height == 0:
                trailheads.append((i, j))
    return trailheads

def find_summits(map_data):
    summits = []
    for i, row in enumerate(map_data):
        for j, height in enumerate(row):
            if height == 9:
                summits.append((i, j))
    return summits

def build_graph(map_data):
    G = nx.DiGraph()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for i, row in enumerate(map_data):
        for j, height in enumerate(row):
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < len(map_data) and 0 <= nj < len(map_data[0]):
                    if map_data[ni][nj] == height + 1:
                        G.add_edge((i, j), (ni, nj))
    return G

def solve_part1(file_path):
    map_data = read_input(file_path)
    trailheads = find_trailheads(map_data)
    summits = find_summits(map_data)
    G = build_graph(map_data)
    return sum(nx.has_path(G, a, b) for a in trailheads for b in summits)

def solve_part2(file_path):
    map_data = read_input(file_path)
    trailheads = find_trailheads(map_data)
    summits = find_summits(map_data)
    G = build_graph(map_data)
    return sum(
        len(list(nx.all_simple_edge_paths(G, a, b)))
        for a in trailheads
        for b in summits
        if nx.has_path(G, a, b)
    )

if __name__ == '__main__':
    file_path = 'data_day10.txt'
    print(f"Part 1: {solve_part1(file_path)}")
    print(f"Part 2: {solve_part2(file_path)}")