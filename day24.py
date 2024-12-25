import re
from itertools import combinations

def read_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    initial_values = {}
    gates = []
    
    for line in lines:
        line = line.strip()
        if ':' in line:
            wire, value = line.split(': ')
            initial_values[wire] = int(value)
        elif '->' in line:
            gates.append(line)
    
    return initial_values, gates

def simulate_gates(initial_values, gates):
    wire_values = initial_values.copy()
    
    while gates:
        new_gates = []
        for gate in gates:
            parts = gate.split(' ')
            if len(parts) == 5:
                input1, operation, input2, _, output = parts
                if input1 in wire_values and input2 in wire_values:
                    if operation == 'AND':
                        wire_values[output] = wire_values[input1] & wire_values[input2]
                    elif operation == 'OR':
                        wire_values[output] = wire_values[input1] | wire_values[input2]
                    elif operation == 'XOR':
                        wire_values[output] = wire_values[input1] ^ wire_values[input2]
                else:
                    new_gates.append(gate)
        gates = new_gates
    
    return wire_values

def calculate_output(wire_values):
    z_wires = {k: v for k, v in wire_values.items() if k.startswith('z')}
    max_index = max(int(k[1:]) for k in z_wires.keys())
    binary_number = ''.join(str(z_wires.get(f'z{i:02}', 0)) for i in range(max_index + 1))
    return int(binary_number[::-1], 2)  # Reverse the binary number to get the correct order

def find_swapped_gates(initial_values, gates):
    gate_pattern = r"([a-z0-9]{3}) ([XORAND]+) ([a-z0-9]{3}) -> ([a-z0-9]{3})"
    ops = set()
    op_list = []
    for line in gates:
        match = re.search(gate_pattern, line)
        x1, op, x2, res = match.groups()
        ops.add((x1, x2, res, op))
        op_list.append((x1, x2, res, op))

    def furthest_made(op_list):
        ops = {}
        for x1, x2, res, op in op_list:
            ops[(frozenset([x1, x2]), op)] = res

        def get_res(x1, x2, op):
            return ops.get((frozenset([x1, x2]), op), None)

        carries = {}
        correct = set()
        prev_intermediates = set()
        for i in range(45):
            pos = f"0{i}" if i < 10 else str(i)
            predigit = get_res(f"x{pos}", f"y{pos}", "XOR")
            precarry1 = get_res(f"x{pos}", f"y{pos}", "AND")
            if i == 0:
                assert predigit == f"z00"
                carries[i] = precarry1
                continue
            digit = get_res(carries[i - 1], predigit, "XOR")
            if digit != f"z{pos}":
                return i - 1, correct

            correct.add(carries[i - 1])
            correct.add(predigit)
            for wire in prev_intermediates:
                correct.add(wire)

            precarry2 = get_res(carries[i - 1], predigit, "AND")
            carry_out = get_res(precarry1, precarry2, "OR")
            carries[i] = carry_out
            prev_intermediates = set([precarry1, precarry2])

        return 45, correct

    swaps = set()

    base, base_used = furthest_made(op_list)
    for _ in range(4):
        for i, j in combinations(range(len(op_list)), 2):
            x1_i, x2_i, res_i, op_i = op_list[i]
            x1_j, x2_j, res_j, op_j = op_list[j]
            if "z00" in (res_i, res_j):
                continue
            if res_i in base_used or res_j in base_used:
                continue
            op_list[i] = x1_i, x2_i, res_j, op_i
            op_list[j] = x1_j, x2_j, res_i, op_j
            attempt, attempt_used = furthest_made(op_list)
            if attempt > base:
                swaps.add((res_i, res_j))
                base, base_used = attempt, attempt_used
                break
            op_list[i] = x1_i, x2_i, res_i, op_i
            op_list[j] = x1_j, x2_j, res_j, op_j

    ans = ",".join(sorted(sum(swaps, start=tuple())))
    return ans

if __name__ == "__main__":
    initial_values, gates = read_input('data_files/data_day24.txt')
    wire_values = simulate_gates(initial_values, gates)
    
    result = calculate_output(wire_values)
    print(f"Part 1 -> {result}")

    result = find_swapped_gates(initial_values, gates)
    print(f"Part 2 -> {result}")
