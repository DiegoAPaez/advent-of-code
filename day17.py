import re

def read_program(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
    return list(map(int, re.findall(r'\d+', data)))

def eval_program(a, b, c, prog):
    i = 0
    R = []
    while i in range(len(prog)):
        C = {0: 0, 1: 1, 2: 2, 3: 3, 4: a, 5: b, 6: c}
        match prog[i:i+2]:
            case 0, op: a = a >> C[op]
            case 1, op: b = b ^ op
            case 2, op: b = 7 & C[op]
            case 3, op: i = op - 2 if a else i
            case 4, op: b = b ^ c
            case 5, op: R = R + [C[op] & 7]
            case 6, op: b = a >> C[op]
            case 7, op: c = a >> C[op]
        i += 2
    return R

def find_lowest_initial_value(prog, b, c):
    def find(a, i):
        if eval_program(a, b, c, prog) == prog:
            #print(a)
            return a
        if eval_program(a, b, c, prog) == prog[-i:] or not i:
            for n in range(8):
                result = find(8 * a + n, i + 1)
                if result is not None:
                    return result
        return None

    return find(0, 0)

if __name__ == "__main__":
    file_path = 'data_files/data_day17.txt'
    data = read_program(file_path)
    a, b, c, *prog = data
    
    # Part 1
    result_part1 = eval_program(a, b, c, prog)
    print("Part 1 Output:", ','.join(map(str, result_part1)))
    
    # Part 2
    result_part2 = find_lowest_initial_value(prog, b, c)
    print("Part 2 Lowest Initial Value for Register A:", result_part2)