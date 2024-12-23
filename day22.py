from collections import defaultdict
from itertools import pairwise

# Define a constant for pruning the secret number
PRUNE = (2 ** 24) - 1

# Function to generate the next secret number based on the current secret
def next_secret_number(secret):
    secret = (secret ^ (secret << 6)) & PRUNE
    secret = (secret ^ (secret >> 5)) & PRUNE
    secret = (secret ^ (secret << 11)) & PRUNE
    return secret

def main():
    # Read initial secret numbers from the input file
    with open('data_files/data_day22.txt') as f:
        initial_secrets = [int(line.strip()) for line in f]

    # Part 1: Calculate the total of the last numbers in the sequences
    total = 0
    sequences = defaultdict(int)

    for initial_secret in initial_secrets:
        # Generate a sequence of 2001 numbers starting from the initial secret
        nums = [initial_secret] + [initial_secret := next_secret_number(initial_secret) for _ in range(2000)]
        total += nums[-1]  # Add the last number in the sequence to the total

        # Calculate the differences between consecutive numbers modulo 10
        diffs = [b % 10 - a % 10 for a, b in pairwise(nums)]

        seen = set()
        # Look for unique patterns of 4 consecutive differences
        for i in range(len(nums) - 4):
            pat = tuple(diffs[i:i + 4])
            if pat not in seen:
                # If the pattern is not seen before, add the 5th number modulo 10 to the sequences dictionary
                sequences[pat] += nums[i + 4] % 10
                seen.add(pat)

    # Print the results for Part 1 and Part 2
    print("Part 1 result ->", total)
    print("Part 2 result -> Most bananas:", max(sequences.values()))

if __name__ == "__main__":
    main()