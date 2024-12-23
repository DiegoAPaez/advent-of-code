from collections import defaultdict
from itertools import combinations

# Step 1: Parse the input data
with open('data_files/data_day23.txt') as f:
    connections = [line.strip().split('-') for line in f]

# Step 2: Build the graph
graph = defaultdict(set)
for a, b in connections:
    graph[a].add(b)
    graph[b].add(a)

# Step 3: Find all sets of three interconnected computers
triangles = set()
for a in graph:
    for b in graph[a]:
        for c in graph[a]:
            if b != c and b in graph[c]:
                triangles.add(tuple(sorted([a, b, c])))

# Step 4: Filter sets containing at least one computer starting with 't'
filtered_triangles = [triangle for triangle in triangles if any(node.startswith('t') for node in triangle)]

# Step 5: Count and return the number of such sets
print("Part 1 ->", len(filtered_triangles))

# Part 2: Find the largest clique using Bron-Kerbosch algorithm
def bron_kerbosch(R, P, X):
    if not P and not X:
        yield R
    while P:
        v = P.pop()
        yield from bron_kerbosch(R.union([v]), P.intersection(graph[v]), X.intersection(graph[v]))
        X.add(v)

nodes = set(graph.keys())
max_clique = max(bron_kerbosch(set(), nodes, set()), key=len)

# Generate the password
password = ','.join(sorted(max_clique))
print("Part 2 ->", password)