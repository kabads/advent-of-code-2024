import re

def parse_and_multiply(input_content):
    # Regular expression to match valid mul(X, Y) instructions
    pattern = r'mul\((\d+),(\d+)\)'
    
    # Find all matches in the input content
    matches = re.findall(pattern, input_content)
    
    # Calculate the sum of the results of the multiplications
    total_sum = 0
    for match in matches:
        x, y = map(int, match)
        total_sum += x * y
    
    return total_sum

if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        input_content = file.read()
    
    result = parse_and_multiply(input_content)
    print(result)
