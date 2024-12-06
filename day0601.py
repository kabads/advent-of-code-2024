from typing import List


def read_map_from_file(file_path: str) -> List[str]:
    with open(file_path, 'r') as file:
        return [line.rstrip('\n') for line in file]


def count_guard_patrol_positions(map_input: List[str]) -> int:
    # Directions: North, East, South, West
    directions = ['^', '>', 'v', '<']
    direction_index = 0  # Start facing North
    visited_positions = set()
 
    # Find the initial position of the guard
    guard_position = None
    for r in range(len(map_input)):
        for c in range(len(map_input[r])):
            if map_input[r][c] in directions:
                guard_position = (r, c)
                direction_index = directions.index(map_input[r][c])  # Set initial direction
                break
        if guard_position:
            break

    if not guard_position:
        return 0  # No guard found

    visited_positions.add(guard_position)
    current_row, current_col = guard_position

    while True:
        # Determine the next position based on the current direction
        if directions[direction_index] == '^':
            next_row, next_col = current_row - 1, current_col
        elif directions[direction_index] == '>':
            next_row, next_col = current_row, current_col + 1
        elif directions[direction_index] == 'v':
            next_row, next_col = current_row + 1, current_col
        elif directions[direction_index] == '<':
            next_row, next_col = current_row, current_col - 1

        # Check if the next position is out of bounds
        if not (0 <= next_row < len(map_input) and 0 <= next_col < len(map_input[0])):
            break  # Guard has left the map

        # Check if the next position is not an obstacle
        if map_input[next_row][next_col] != '#':
            # Move to the next position
            current_row, current_col = next_row, next_col
            visited_positions.add((current_row, current_col))
        else:
            # Turn right (change direction)
            direction_index = (direction_index + 1) % 4

    return len(visited_positions)


if __name__ == "__main__":
    map_input = read_map_from_file('input.txt')
    unique_positions_count = count_guard_patrol_positions(map_input)
    print(unique_positions_count)  # Expected output: 41
