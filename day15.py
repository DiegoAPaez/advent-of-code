from collections import defaultdict

def parse_input(map_file, moves_file):
    with open(map_file, 'r') as f:
        warehouse_map = f.read()
    
    with open(moves_file, 'r') as f:
        moves = f.read().replace('\n', '')
    
    return warehouse_map, moves

def parse_content(warehouse_map, moves):
    grid = defaultdict(str) | {
        (y + x * 1j): cell
        for y, line in enumerate(warehouse_map.splitlines())
        for x, cell in enumerate(line)
    }
    move_directions = [{'^': -1, '>': 1j, 'v': 1, '<': -1j}[move] for move in moves]
    return grid, move_directions

def simulate_movements(grid, move_directions):
    robot_position = next(position for position, value in grid.items() if value == '@')
    for direction in move_directions:
        to_move = []
        queue = [robot_position]
        while queue:
            current_position = queue.pop()
            if grid[current_position] in ['#', '']:
                break
            elif grid[current_position] != '.':
                to_move.append(current_position)
                next_position = current_position + direction
                queue.append(next_position)
                if not direction.imag and grid[next_position] == '[':
                    queue.append(next_position + 1j)
                if not direction.imag and grid[next_position] == ']':
                    queue.append(next_position - 1j)
        else:
            seen_positions = set()
            for position in reversed(to_move):
                if position not in seen_positions:
                    seen_positions.add(position)
                    grid[position], grid[position + direction] = grid[position + direction], grid[position]
            robot_position += direction

def calculate_gps_coordinates(grid, box_char):
    return sum(position.real * 100 + position.imag for position in grid if grid[position] == box_char)

def simulate_warehouse(map_file, moves_file):
    warehouse_map, moves = parse_input(map_file, moves_file)
    grid, move_directions = parse_content(warehouse_map, moves)
    simulate_movements(grid, move_directions)
    return calculate_gps_coordinates(grid, 'O')

def simulate_scaled_warehouse(map_file, moves_file):
    warehouse_map, moves = parse_input(map_file, moves_file)
    scaled_map = warehouse_map.replace('O', '[]').replace('.', '..').replace('#', '##').replace('@', '@.')
    grid, move_directions = parse_content(scaled_map, moves)
    simulate_movements(grid, move_directions)
    return calculate_gps_coordinates(grid, '[')

# Example usage
map_file = 'data_files/data_day15_map.txt'
moves_file = 'data_files/data_day15_moves.txt'

# Part 1
print("Part 1:", int(simulate_warehouse(map_file, moves_file)))

# Part 2
print("Part 2:", int(simulate_scaled_warehouse(map_file, moves_file)))