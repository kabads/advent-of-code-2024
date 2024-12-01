def separate_nums(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    left_list = []
    right_list = []
    for line in lines:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)

    return left_list, right_list

def sort_lists(left_list, right_list):
    left_list.sort()
    right_list.sort()
    return left_list, right_list

def compare_lists(left_list, right_list):
    differences = []
    for l, r in zip(left_list, right_list):
        difference = abs(l - r)
        differences.append(difference)
    return differences

def count_list_frequency(left_list, right_list):
    frequency_dict = {}
    for num in right_list:
        if num in frequency_dict:
            frequency_dict[num] += 1
        else:
            frequency_dict[num] = 1

    result = []
    for num in left_list:
        if num in frequency_dict:
            result.append(num * frequency_dict[num])
        else:
            result.append(0)

    return result

if __name__ == '__main__':
    left, right = separate_nums('1-input.txt')
    # print(f"Original Left list: {left}")
    # print(f"Original Right list: {right}")

    left, right = sort_lists(left, right)
    # print(f"Sorted Left list: {left}")
    # print(f"Sorted Right list: {right}")

    differences = compare_lists(left, right)
    # print(f"Differences between lists: {differences}")

    total_difference = sum(differences)
    print(f"Total difference: {total_difference}")


    frequency_result = count_list_frequency(left, right)
    total_frequency = sum(frequency_result)
    print(f"Total frequency: {total_frequency}")
