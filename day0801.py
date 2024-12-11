def parse_antenna_map(input_data):
    antenna_locations = {}
    for y, row in enumerate(input_data):
        for x, char in enumerate(row):
            if char != '.':
                if char not in antenna_locations:
                    antenna_locations[char] = []
                antenna_locations[char].append((x, y))
    return antenna_locations


def find_antinodes(antenna_map, max_x, max_y):
    antinodes = set()
    for frequency, locations in antenna_map.items():
        for i in range(len(locations)):
            for j in range(i + 1, len(locations)):
                x1, y1 = locations[i]
                x2, y2 = locations[j]

                # Calculate potential antinode locations
                antinode1_x = 2 * x1 - x2
                antinode1_y = 2 * y1 - y2
                antinode2_x = 2 * x2 - x1
                antinode2_y = 2 * y2 - y1

                # Check if antinodes are within the map bounds
                if 0 <= antinode1_x <= max_x and 0 <= antinode1_y <= max_y:
                    antinodes.add((antinode1_x, antinode1_y))
                if 0 <= antinode2_x <= max_x and 0 <= antinode2_y <= max_y:
                    antinodes.add((antinode2_x, antinode2_y))

    return antinodes


def main():
    with open("input.txt", "r") as f:
        input_data = f.readlines()

    input_data = [line.rstrip('\n') for line in input_data]
    max_x = len(input_data[0]) - 1 if input_data else 0
    max_y = len(input_data) - 1
    antenna_map = parse_antenna_map(input_data)
    antinodes = find_antinodes(antenna_map, max_x, max_y)
    print(len(antinodes))


if __name__ == "__main__":
    main()
