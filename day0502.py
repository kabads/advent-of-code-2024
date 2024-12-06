import statistics
from collections import defaultdict


def parse_input(input_text):
    lines = input_text.strip().split('\n')
    rules = defaultdict(list)
    updates = []

    # Parse rules
    for line in lines:
        if '|' in line:
            a, b = map(int, line.split('|'))
            rules[a].append(b)
        elif ',' in line:
            updates.append(list(map(int, line.split(','))))

    return rules, updates


def is_valid_order(update, rules):
    position = {page: idx for idx, page in enumerate(update)}
    for a in rules:
        for b in rules[a]:
            if a in position and b in position:
                if position[a] > position[b]:
                    return False
    return True


def find_middle_page(update):
    n = len(update)
    if n % 2 == 1:
        return update[n // 2]
    else:
        return statistics.median(update)


def reorder_update(update, rules):
    # Topological sorting using depth-first search
    def build_graph(update, rules):
        graph = defaultdict(set)
        # Consider all possible rules for the pages in the update
        for page in update:
            for other_page in update:
                if page in rules and other_page in rules[page]:
                    graph[other_page].add(page)
        return graph

    def topological_sort(update, graph):
        nodes = set(update)
        result = []
        unvisited = set(update)

        def visit(n):
            if n not in unvisited:
                return
            for nbr in graph[n]:
                if nbr not in nodes:
                    continue
                visit(nbr)
            unvisited.remove(n)
            result.append(n)

        while unvisited:
            for x in unvisited:
                break
            visit(x)

        return result[::-1]

    graph = build_graph(update, rules)
    return topological_sort(update, graph)


def solve_part1(rules, updates):
    middle_pages = []
    for update in updates:
        if is_valid_order(update, rules):
            middle_pages.append(find_middle_page(update))
    return sum(middle_pages)


def solve_part2(rules, updates):
    middle_pages = []
    for update in updates:
        if not is_valid_order(update, rules):
            reordered = reorder_update(update, rules)
            middle_pages.append(find_middle_page(reordered))
    return sum(middle_pages)


def main():
    with open('input.txt', 'r') as f:
        input_text = f.read()

    rules, updates = parse_input(input_text)

    part1_result = solve_part1(rules, updates)
    part2_result = solve_part2(rules, updates)
    print("Part 1:", part1_result)
    print("Part 2:", part2_result)


if __name__ == '__main__':
    main()
