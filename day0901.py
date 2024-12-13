def disk_read():
    filesystem = []
    with open("input.txt", "r") as file:
        for line in file:
            for char in line:
                if char.isdigit():
                    filesystem.append(int(char))
    return filesystem


def parse_filesystem(filesystem):
    parsed_list = []
    for i in range(0, len(filesystem) - 1, 2):
        parsed_list.append((filesystem[i], filesystem[i+1]))
    if len(filesystem) % 2 != 0:
        parsed_list.append((filesystem[-1], 0))
    return parsed_list


def build_fs_map(parsed_list):
    filesystem_map = []
    for index, (even, odd) in enumerate(parsed_list):
        current_id = index
        filesystem_map.extend([current_id] * even)
        filesystem_map.extend([None] * odd)
    return filesystem_map


def defrag(filesystem_map):
    next_digit_index = len(filesystem_map) - 1
    for i in range(len(filesystem_map)):
        if filesystem_map[i] is None:
            while next_digit_index > i:
                if isinstance(filesystem_map[next_digit_index], int):
                    filesystem_map[i], filesystem_map[next_digit_index] = filesystem_map[next_digit_index], filesystem_map[i]
                    next_digit_index -= 1
                    break
                next_digit_index -= 1
    return filesystem_map


def calculate_hash(defragged_list):
    hash_value = 0
    id = 0
    for char in defragged_list:
        if isinstance(char, int):
            hash_value += id * char
        id += 1
    return hash_value


if __name__ == '__main__':
    filesystem = disk_read()
    parsed_list = parse_filesystem(filesystem)
    filesystem_map = build_fs_map(parsed_list)
    defragged_map = defrag(filesystem_map)

    hash_value = calculate_hash(defragged_map)
    print(hash_value)
