file_path = 'data_day4.txt'

def find_xmas_in_file(file_path, word="XMAS"):
    # Read the file and convert it into a grid (list of strings)
    with open(file_path, 'r') as file:
        grid = [line.strip() for line in file.readlines()]
    
    rows = len(grid)
    cols = len(grid[0])
    word_len = len(word)
    
    # Directions: (row_offset, col_offset)
    directions = [
        (0, 1),   # Right
        (0, -1),  # Left
        (1, 0),   # Down
        (-1, 0),  # Up
        (1, 1),   # Diagonal down-right
        (-1, -1), # Diagonal up-left
        (1, -1),  # Diagonal down-left
        (-1, 1)   # Diagonal up-right
    ]
    
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def search_from(x, y, direction):
        dx, dy = direction
        for i in range(word_len):
            nx, ny = x + i * dx, y + i * dy
            if not is_valid(nx, ny) or grid[nx][ny] != word[i]:
                return False
        return True

    count = 0
    for r in range(rows):
        for c in range(cols):
            for direction in directions:
                if search_from(r, c, direction):
                    count += 1
    
    return count

def find_x_mas_in_file(file_path):
    with open(file_path, 'r') as file:
        grid = [line.strip() for line in file.readlines()]
    
    rows = len(grid)
    cols = len(grid[0])

    def is_word(y, x, dy, dx, word):
        for i, char in enumerate(word):
            j = y + i * dy
            k = x + i * dx
            if not (0 <= j < rows and 0 <= k < cols and grid[j][k] == char):
                return False
        return True

    def is_x_mas(y, x):
        top_left = is_word(y, x, 1, 1, "MAS") or is_word(y, x, 1, 1, "SAM")
        top_right = is_word(y, x + 2, 1, -1, "MAS") or is_word(y, x + 2, 1, -1, "SAM")
        return top_left and top_right

    return sum(is_x_mas(y, x) for y in range(rows) for x in range(cols))


result_part1 = find_xmas_in_file(file_path)
print(f"Total occurrences of XMAS: {result_part1}")

result_part2 = find_x_mas_in_file(file_path)
print(f"Total occurrences of X-MAS: {result_part2}")