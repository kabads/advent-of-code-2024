import math


def parse_antenna_map(input_data):
    antenna_locations = {}
    for y, row in enumerate(input_data):
        for x, char in enumerate(row):
            if char != '.':
                if char not in antenna_locations:
                    antenna_locations[char] = []
                antenna_locations[char].append((x, y))
    return antenna_locations
import math


def is_collinear(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return (y1 - y2) * (x1 - x3) == (y1 - y3) * (x1 - x2)


def find_antinodes(antenna_map, max_x, max_y, exclude_single_frequency=False):
    antinodes = set()
    for frequency, locations in antenna_map.items():
        if exclude_single_frequency and len(locations) < 2:
            continue

        for i in range(len(locations)):
            for j in range(i + 1, len(locations)):
                x1, y1 = locations[i]
                x2, y2 = locations[j]
                dx = x2 - x1
                dy = y2 - y1
                gcd = math.gcd(dx, dy)
                gcd_vec = (dx // gcd, dy // gcd)

                # Extend from locations[i] in both directions
                x, y = x1, y1
                while 0 <= x <= max_x and 0 <= y <= max_y:
                    antinodes.add((x, y))
                    x, y = x - gcd_vec[0], y - gcd_vec[1]

                x, y = x1 + gcd_vec[0], y1 + gcd_vec[1]
                while 0 <= x <= max_x and 0 <= y <= max_y:
                    antinodes.add((x, y))
                    x, y = x + gcd_vec[0], y + gcd_vec[1]
    return antinodes


def main():
    with open("input.txt", "r") as f:
        input_data = f.readlines()

    input_data = [line.rstrip('\n') for line in input_data]
    max_x = len(input_data[0]) - 1 if input_data else 0
    max_y = len(input_data) - 1

    antenna_map_part2 = parse_antenna_map(input_data)
    antinodes_part2 = find_antinodes(antenna_map_part2, max_x, max_y, exclude_single_frequency=True)
    print(f"{len(antinodes_part2)}")


if __name__ == "__main__":
    main()
