def read_file(filename):
    with open(filename, 'r') as file:
        return [list(line.strip()) for line in file.readlines()]


def inbounds(i, j, length):
    return 0 <= i < length and 0 <= j < length


grid = read_file('input.txt')
length_of_grid = len(grid)  # Create a variable that holds the length of grid
count = 0  # Initialize the count variable

# Define diagonal offsets
diagonal_offsets = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

for i in range(length_of_grid):
    for j in range(length_of_grid):
        if grid[i][j] != "A":
            continue

        # Check bounds for all diagonal directions
        if not all(inbounds(i + di, j + dj, length_of_grid) for di, dj in diagonal_offsets):
            continue

        # Check diagonal elements
        if not (grid[i - 1][j - 1], grid[i + 1][j + 1]) in (('M', 'S'), ('S', 'M')):
            continue
        if not (grid[i - 1][j + 1], grid[i + 1][j - 1]) in (('M', 'S'), ('S', 'M')):
            continue

        count += 1  # Add one to the count variable when conditions are met

print(count)  # Print the final count
