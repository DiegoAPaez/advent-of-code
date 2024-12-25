def solve(data):
    keys = []
    locks = []
    
    # Process each block of data
    for block in data:
        # Convert each line in the block to a binary number
        binary_representation = [int("".join("1" if x == "#" else "0" for x in line), 2)
                                 for line in zip(*block)]
        
        # Determine if the block is a key or a lock
        if block[0][0] == '.':
            keys.append(binary_representation)
        else:
            locks.append(binary_representation)
    
    valid_pairs_count = 0
    
    # Check each lock against each key
    for lock in locks:
        for key in keys:
            # Ensure no overlapping pins using bitwise AND
            if all(lock_pin & key_pin == 0 for lock_pin, key_pin in zip(lock, key)):
                valid_pairs_count += 1
    
    return valid_pairs_count

def main():
    # Read input file
    with open('data_files/data_day25.txt', 'r') as file:
        data = [block.split('\n') for block in file.read().strip().split('\n\n')]
    
    # Solve the problem
    result = solve(data)
    
    # Print the result
    print("Part 1 ->", result)

if __name__ == "__main__":
    main()