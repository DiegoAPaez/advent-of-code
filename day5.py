from collections import defaultdict, deque

def parse_input(file_path):
    with open(file_path, 'r') as file:
        data = file.read().strip().split('\n\n')
    
    # First section: ordering rules
    rules = [tuple(map(int, line.split('|'))) for line in data[0].split('\n')]
    
    # Second section: updates
    updates = [list(map(int, line.split(','))) for line in data[1].split('\n')]
    
    return rules, updates

def is_update_ordered(update, rules):
    # Map page numbers to their positions in the update
    position = {page: idx for idx, page in enumerate(update)}
    
    # Check each rule X|Y
    for x, y in rules:
        if x in position and y in position:  # Rule applies only if both pages are in the update
            if position[x] >= position[y]:  # X must appear before Y
                return False
    return True

# Topological sort for reordering an update
def reorder_update(update, rules):
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    pages = set(update)
    
    # Build the graph for pages in the update
    for x, y in rules:
        if x in pages and y in pages:
            graph[x].append(y)
            in_degree[y] += 1
            if x not in in_degree:
                in_degree[x] = 0
    
    # Perform topological sort
    queue = deque([node for node in pages if in_degree[node] == 0])
    sorted_order = []
    
    while queue:
        current = queue.popleft()
        sorted_order.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return sorted_order

def find_middle_page(update):
    return update[len(update) // 2]  # Middle page (floor division)

def calculate_sum(file_path):
    # Parse input
    rules, updates = parse_input(file_path)
    
    # Check updates and calculate the sum of middle pages for correctly ordered updates
    total_sum = 0
    for update in updates:
        if is_update_ordered(update, rules):
            total_sum += find_middle_page(update)
    
    return total_sum

def calculate_sum_for_incorrect(file_path):
    rules, updates = parse_input(file_path)
    total_sum = 0
    
    for update in updates:
        if not is_update_ordered(update, rules):  # Check if the update is incorrect
            reordered = reorder_update(update, rules)  # Reorder the update
            total_sum += find_middle_page(reordered)  # Add the middle page of the reordered update
    
    return total_sum

file_path = 'data_day5.txt'
result_part1 = calculate_sum(file_path)
print(f"PART 1 - Total Sum of Middle Pages: {result_part1}")

result_part2 = calculate_sum_for_incorrect(file_path)
print(f"PART 2 - Total Sum of Middle Pages: {result_part2}")