def parse_and_multiply_with_conditions(input_content):
    # Regular expressions to match do() and don't() instructions
    do_pattern = r'do\(\)'
    dont_pattern = r"don't\(\)"
    
    # Calculate the sum of results of just the enabled multiplications
    total_sum = 0
    enabled = True
    
    # Split the input content into parts based on do() and don't()
    import re
    parts = re.split(r'(do\(\)|don\'t\(\))', input_content)
    
    for part in parts:
        if 'do()' in part:
            enabled = True
        elif "don't()" in part:
            enabled = False
        else:
            # Find all mul(x, y) instructions in the current part
            matches = re.findall(r'mul\((\d+),(\d+)\)', part)
            for match in matches:
                x, y = map(int, match)
                if enabled:
                    total_sum += x * y
    
    return total_sum

if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        input_content = file.read()
    
    result = parse_and_multiply_with_conditions(input_content)
    print(result)
