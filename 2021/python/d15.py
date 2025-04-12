# d15.py
# Advent of Code 2021 day 15 ver 1
# https://adventofcode.com/2021/day/15
# Chitons: Shortest weighted path

import networkx as nx
from networkx.algorithms.shortest_paths import single_source_dijkstra


def part1(input_file):
    dist, path = shortest_dist(prep_data(input_file))
    # print(path)
    return dist


def part2(input_file):
    tiled = extend_tiles(prep_data(input_file), 5)
    dist, path = shortest_dist(tiled)
    # print(path)
    return dist


def shortest_dist(dat):
    nr = len(dat)
    nc = len(dat[0])
    # directed graph
    graph = nx.DiGraph()
    # horizontal neighbors
    for j in range(nr):
        for i in range(nc - 1):
            idx = j * nc + i
            graph.add_edge(idx, idx + 1, weight=dat[j][i + 1])

        for i in range(1, nc):
            idx = j * nc + i
            graph.add_edge(idx, idx - 1, weight=dat[j][i - 1])

    # vertical neighbors
    for i in range(nc):
        for j in range(nr - 1):
            ids = j * nc + i
            idd = (j + 1) * nc + i
            graph.add_edge(ids, idd, weight=dat[j + 1][i])
        for j in range(1, nr):
            ids = j * nc + i
            idd = (j - 1) * nc + i
            graph.add_edge(ids, idd, weight=dat[j - 1][i])

    print(graph)
    # start and end points
    beg, end = 0, nr * nc - 1
    dist, path = single_source_dijkstra(graph, beg, end, weight="weight")

    return dist, path


def extend_tiles(dat, ntile=5):
    def roll_over(x):
        y = x % 9
        return y if y != 0 else 9

    tiled = []
    for row in dat:
        across = []
        for bi in range(ntile):
            block = list(map(roll_over, list(map(lambda x: x + bi, row))))
            across.extend(block)
        tiled.append(across)

    first_block = tiled.copy()
    for bi in range(1, ntile):
        for row in first_block:
            block = list(map(roll_over, list(map(lambda x: x + bi, row))))
            tiled.append(block)

    return tiled


def read_groups(input_file, sep="\n"):
    with open(input_file, "r") as fn:
        buf = fn.read()
    return [e.strip() for e in buf.split(sep) if len(e.strip()) > 0]


def prep_data(input_file):
    dat = read_groups(input_file)
    dat = [list(map(int, list(r))) for r in dat]
    return dat


if __name__ == "__main__":

    valid_file = "data/15a.txt"
    input_file = "data/15.txt"

    # part 1
    assert part1(valid_file) == 40
    assert part1(input_file) == 363

    # part 2
    assert part2(valid_file) == 315
    assert part2(input_file) == 2835
