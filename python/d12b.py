# d12.py
# Advent of Code 2021 day 12 ver 1
# https://adventofcode.com/2021/day/12
# Passage pathing: 

import networkx as nx


def all_paths_util(g, u, d, visited, path, count):
    visited[u] = True
    count[u] += 1
    path.append(u)

    if u == d:
        print(path)
    else:
        for i in g[u]:
            if visited[i] is False or i.isupper() or (i.islower() and count[u] <= 2 and i!= "start" and i!= "end"):
                all_paths_util(g, i, d, visited, path, count)

    path.pop()
    visited[u] = False


def all_paths(g, s, d):

    visited = {}
    for k in g.nodes:
        visited[k] = False

    count = {}
    for k in g.nodes:
        count[k] = 0

    path = []
    all_paths_util(g, s, d, visited, path, count)


def part1(input_file):
    dat = prep_data(input_file)

    # print(dat)

    g = nx.Graph(dat)
    # print(g)

    all_paths(g, "start", "end")

    return len(dat)


# def part2(input_file):
#     dat = prep_data(input_file)

#     return len(dat)


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
    # valid_file = "data/12b.txt"
    # valid_file = "data/12c.txt"
    # input_file = "data/12.txt"

    # part 1
    # assert part1(valid_file) == 0
    # print(part1(valid_file))
    part1(valid_file)
    # part1(input_file)
    # assert part1(input_file) == 0
    # print("part 1:", part1(input_file))

    # part 2
    # assert part2(valid_file) == 0
    # print(part2(valid_file))
    # assert part2(input_file) == 0
    # print("part 2:", part2(input_file))
