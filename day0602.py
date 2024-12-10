from dataclasses import dataclass


def read_map_from_file(filename):
    """Read the map from input file and return the grid and guard position"""
    grid = []
    start = None
    with open(filename, 'r') as f:
        for i, line in enumerate(f.readlines()):
            row = line.strip()
            if '^' in row:
                start = (i, row.find('^'))
                row = row.replace('^', '.')
            grid.append(row)
    return grid, start


@dataclass(frozen=True)
class Pos:
    i: int
    j: int
    def __add__(self, other):
        return Pos(self.i + other.i, self.j + other.j)
    def __eq__(self, other):
        return isinstance(other, Pos) and (self.i, self.j) == (other.i, other.j)
    def __hash__(self):
        return hash((self.i, self.j))
    def rotate_right(self):
        return Pos(self.j, -self.i)


def is_inbounds(p, n, m):
    """Check if position is within grid bounds"""
    return 0 <= p.i < n and 0 <= p.j < m


def get_guard_span(grid, start, new_obstacle=None):
    """Simulate guard movement and return visited positions"""
    n = len(grid)
    m = len(grid[0])
    pos = Pos(start[0], start[1])
    direction = Pos(-1, 0)  # up
    visited = set()
    states = {(pos, direction)}

    while is_inbounds(pos, n, m):
        visited.add(pos)
        # try to take a step
        dest = pos + direction
        if (is_inbounds(dest, n, m) and 
            (grid[dest.i][dest.j] == '#' or dest == new_obstacle)):
            # turn right
            direction = direction.rotate_right()
        else:
            # step forward
            pos = dest
        new_state = (pos, direction)
        if new_state in states:
            # infinite loop detected
            return True, visited
        states.add(new_state)
    return False, visited


def main():
    # Read input map
    grid, start = read_map_from_file('input.txt')

    # Part 1: Get initial guard span
    success, visited = get_guard_span(grid, start)
    print(f"Number of positions visited by guard: {len(visited)}")

    # Part 2: Count valid new obstacle positions
    result = 0
    start_pos = Pos(start[0], start[1])
    obstacle_candidates = visited - {start_pos}

    for obstacle in obstacle_candidates:
        if get_guard_span(grid, start, obstacle)[0]:
            result += 1

    print(f"Number of valid new obstacle positions: {result}")

if __name__ == "__main__":
    main()
