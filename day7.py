import itertools

def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    equations = []
    for line in lines:
        parts = line.strip().split(':')
        test_value = int(parts[0])
        numbers = list(map(int, parts[1].strip().split()))
        equations.append((test_value, numbers))
    return equations

def evaluate_expression(numbers, operators):
    result = numbers[0]
    for i in range(1, len(numbers)):
        if operators[i-1] == '+':
            result += numbers[i]
        elif operators[i-1] == '*':
            result *= numbers[i]
        elif operators[i-1] == '||':
            result = int(str(result) + str(numbers[i]))
    return result

def can_be_true(test_value, numbers, part=1):
    operators = ['+', '*'] if part == 1 else ['+', '*', '||']
    for ops in itertools.product(operators, repeat=len(numbers)-1):
        result = evaluate_expression(numbers, ops)
        if result == test_value:
            return True
    return False

def total_calibration_result(file_path, part=1):
    equations = read_input(file_path)
    total = 0
    for test_value, numbers in equations:
        if can_be_true(test_value, numbers, part):
            total += test_value
    return total

# Example usage:
file_path = 'data_day7.txt'
print("Part 1 result:", total_calibration_result(file_path, 1))
print("Part 2 result:", total_calibration_result(file_path, 2))