def order_rules(filename):
    rules = []
    with open(filename, 'r') as file:
        for line in file:
            if line.strip() == "":  # Check for a blank line
                return rules  # Return the rules found so far
            parts = line.strip().split('|')
            if len(parts) == 2:
                rules.append([int(parts[0]), int(parts[1])])  # Store as a list of pairs
    return rules  # Return the rules if no blank line is found

def read_after_whitespace(filename):
    lists = []
    with open(filename, 'r') as file:
        for line in file:
            if line.strip() == "":  # Check for a blank line
                break  # Stop reading when a blank line is found
        for line in file:  # Read the rest of the file
            if line.strip():  # Check if the line is not empty
                lists.append([int(num) for num in line.strip().split(',')])  # Create a list of integers
    return lists

def sum_of_middle_elements(sorted_lists):
    total = 0
    for lst in sorted_lists:
        if lst:  # Check if the list is not empty
            middle_index = len(lst) // 2  # Find the middle index
            total += lst[middle_index]  # Add the middle element to the total
    return total

def remove_invalid_lists(lists_after_whitespace, rules):
    valid_lists = []
    
    # Create a mapping of rules for easy access
    rule_map = {pair[0]: pair[1] for pair in rules}
    
    for lst in lists_after_whitespace:
        is_valid = True
        for rule_start, rule_end in rules:
            if rule_start in lst and rule_end in lst:
                if lst.index(rule_start) > lst.index(rule_end):
                    is_valid = False
                    break
        if is_valid:
            valid_lists.append(lst)
    
    return valid_lists

def main():
    filename = 'input.txt'  # Changed from 'test-input.txt' to 'input.txt'
    rules = order_rules(filename)
    print(rules)  # This will now print a list of pairs

    lists_after_whitespace = read_after_whitespace(filename)
    
    # Print each list in lists_after_whitespace on a new line
    for lst in lists_after_whitespace:
        print(lst)  # Print each list on a new line

    # Call the new function to remove invalid lists
    good_lists = remove_invalid_lists(lists_after_whitespace, rules)

    # Print the valid lists, one per line with line numbers
    for index, lst in enumerate(good_lists, start=1):
        print(f"{index}: {lst}")  # Print each valid list with its line number

    # Calculate the sum of middle elements from the valid lists
    total_middle_sum = sum_of_middle_elements(good_lists)
    
    # Print the total sum of middle elements
    print(f"Total sum of middle elements: {total_middle_sum}")

if __name__ == '__main__':
    main()
