import re
import numpy as np
from typing import List, Tuple
from itertools import starmap

def read_machine_data(file_name: str) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    with open(file_name, 'r') as file:
        lines = file.readlines()
    
    data = []
    for i in range(0, len(lines), 4):  # Adjusting the step to 4 to account for the blank line
        if lines[i].strip() == '':  # Skip empty lines
            continue
        
        def extract_values(line: str) -> Tuple[int, int]:
            x_value = int(re.search(r'X[+=](\d+)', line).group(1))
            y_value = int(re.search(r'Y[+=](\d+)', line).group(1))
            return (x_value, y_value)
        
        button_a = extract_values(lines[i])
        button_b = extract_values(lines[i+1])
        prize = extract_values(lines[i+2])
        
        data.extend([button_a, button_b, prize])
    
    data = np.array(data).reshape(-1, 2)
    AS = data[::3]
    BS = data[1::3]
    PRIZES = data[2::3]
    
    return AS, BS, PRIZES

def linear_combination(a: np.ndarray, b: np.ndarray, x: np.ndarray) -> int:
    M = np.stack([a, b])
    try:
        s = (np.linalg.solve(M.T, x) + 0.5).astype(int)
        return s @ (3, 1) if (s @ M == x).all() else 0
    except np.linalg.LinAlgError:
        return 0

def main(part: int):
    part = part
    AS, BS, PRIZES = read_machine_data('data_files/data_day13.txt')
    
    if part == 2:
        PRIZES += 10000000000000
    
    total_min_tokens = sum(starmap(linear_combination, zip(AS, BS, PRIZES)))
    prizes_won = np.count_nonzero([linear_combination(a, b, p) for a, b, p in zip(AS, BS, PRIZES)])
    
    print(f"------ PART {part} ------ ")
    print(f'Total prizes won: {prizes_won}')
    print(f'Total minimum tokens required: {total_min_tokens}')

if __name__ == "__main__":
    main(1)
    main(2)