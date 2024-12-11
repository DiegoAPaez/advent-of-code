def process_file(file_path):
    left_column = []
    right_column = []
    
    # Read the file and populate the arrays
    with open(file_path, 'r') as file:
        for line in file:
            left, right = map(int, line.split())  # Split and convert to integers
            left_column.append(left)
            right_column.append(right)
    
    # Sort both arrays
    left_column.sort()
    right_column.sort()
    
    # Calculate the total difference
    total_difference = 0
    for left, right in zip(left_column, right_column):
        total_difference += abs(left - right)  # Add the absolute difference
    
    print("Part 1 result:", total_difference)

    # Calculate total_occurrences
    total_occurrences = 0
    for left in left_column:
        occurrences = right_column.count(left)  # Count occurrences of 'left' in 'right_column'
        total_occurrences += left * occurrences

    print("Part 2 result:", total_occurrences)


process_file('data_files/data_day1.txt')