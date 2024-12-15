import re

# Read the input file and parse the robots' initial positions and velocities
# Each line in the file is expected to be in the format: p=x,y v=x,y
robots = [[*map(int, re.findall(r'-?\d+', line))] for line in open('data_files/data_day14.txt')]

# Define a lambda function to simulate the movement of robots after t seconds
# The function calculates the new positions considering the wrapping around the edges
simulate_positions = lambda t: [((px + vx * t) % width, (py + vy * t) % height) for px, py, vx, vy in robots]

# Define a lambda function to compare two values
# Returns 1 if a > b, -1 if a < b, and 0 if a == b
compare = lambda a, b: (a > b) - (a < b)

# Define the width and height of the space
width, height = 101, 103

# Initialize a list to count the number of robots in each quadrant
# The list has 9 elements to account for all possible comparisons
quadrant_counts = [0] * 9

# Simulate the positions of the robots after 100 seconds
# Count the number of robots in each quadrant
for pos_x, pos_y in simulate_positions(t=100):
    quadrant_counts[3 * compare(pos_x, width // 2) + compare(pos_y, height // 2)] += 1

# Calculate and print the safety factor
# The safety factor is the product of the counts of robots in the four quadrants
print("Safety factor after 100 seconds:", quadrant_counts[2] * quadrant_counts[4] * quadrant_counts[-4] * quadrant_counts[-2])

# Find the fewest number of seconds required for all robots to have unique positions
# Iterate over time t from 0 to 9,999
for time in range(10_000):
    # Simulate the positions of the robots at time t
    # Check if all positions are unique by comparing the length of the set of positions to the number of robots
    if len(set(simulate_positions(time))) == len(robots):
        # Print the time t and break the loop if all positions are unique
        print("Seconds to display the Easter Egg:", time)
        break