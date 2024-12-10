from itertools import product


def read_file_and_split(filename):
    result = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if ':' in line:
                part1, part2 = line.split(':', 1)
                part1 = part1.strip()
                part2 = part2.strip().split()
                result.append([int(part1), [int(num) for num in part2]])
    return result


def is_valid_equation(target, numbers):
    for operators in product(['+', '*'], repeat=len(numbers)-1):
        value = numbers[0]
        for i, op in enumerate(operators):
            if op == '+':
                value += numbers[i+1]
            else:  # op == '*'
                value *= numbers[i+1]
            if value > target:  # Early exit if we exceed target
                break
        if value == target:
            return True
    return False


if __name__ == '__main__':
    filename = 'input.txt'
    data = read_file_and_split(filename)
    total_count = 0
    total_items = len(data)

    for index, item in enumerate(data):
        if is_valid_equation(item[0], item[1]):
            total_count += item[0]
        progress = (index + 1) / total_items * 100
        print(f"Progress: {progress:.2f}%")
    print(total_count)
