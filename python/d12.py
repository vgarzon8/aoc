# d12.py
# Advent of Code 2021 day 12 ver 1
# https://adventofcode.com/2021/day/12
# Passage paths

# Source: https://github.com/AxlLind/AdventOfCode2021/blob/main/src/bin/12.rs

import networkx as nx


def count_util(graph, src, path, seen_twice):
    if src == "end":
        return 1

    if src.islower() and src in path:
        if seen_twice or src == "start":
            return 0

        seen_twice = True

    path.append(src)
    ans = sum([count_util(graph, i, path, seen_twice) for i in graph[src]])
    path.pop()

    return ans


def count_paths(input_file, mode="part1"):
    graph = nx.Graph(prep_data(input_file))
    print(graph)

    seen_twice = True if mode == "part1" else False
    count = count_util(graph, "start", [], seen_twice)

    return count


def read_lines(input_file):
    with open(input_file, "r") as fn:
        buf = fn.read()
    return [e.strip() for e in buf.split('\n') if len(e.strip()) > 0]


def prep_data(input_file):
    dat = read_lines(input_file)
    dat = [d.split("-") for d in dat]
    return dat


if __name__ == "__main__":

    valid_file = "data/12a.txt"
    input_file = "data/12.txt"

    # part 1
    assert count_paths(valid_file) == 10
    assert count_paths(input_file) == 3450

    # part 2
    assert count_paths(valid_file, "part2") == 36
    assert count_paths(input_file, "part2") == 96528
