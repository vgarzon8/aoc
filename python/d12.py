# d12.py
# Advent of Code 2021 day 12 ver 1
# https://adventofcode.com/2021/day/12
# Passage pathing: 

import networkx as nx


def all_paths_util(g, u, d, visited, path):
    visited[u] = True
    path.append(u)

    if u == d:
        print(path)
    else:
        for i in g[u]:
            if visited[i] is False or i.isupper():
                all_paths_util(g, i, d, visited, path)

    path.pop()
    visited[u] = False


def all_paths(g, s, d):

    visited = {}
    for k in g.nodes:
        visited[k] = False

    path = []
    all_paths_util(g, s, d, visited, path)



def part1(input_file):
    dat = prep_data(input_file)

    # print(dat)

    # # g = nx.Graph([("start", "A"), ("A", "B"), ("start", "B"), ("A", "end"), ("B", "end")])

    g = nx.Graph(dat)
    # print(g)

    # for path in sorted(nx.all_simple_edge_paths(g, "start", "end")):
    #     print(path)

    # for path in sorted(nx.all_simple_paths(g, "start", "end")):
    #     print(path)


    # print(list(g.nodes))
    # print(list(g.edges))
    # print(g.degree)
    # print(g.adj)
    # print(list(g["start"]))

    # paths = []

    # for n in g["start"]:s
    #     for p in g[n]:
    #         for q in g[p]:
    #             for r in g[q]:
    #                 print(n, p, q, r)

    # paths = ["start"]
    # for n in g["start"]:
    #     print(n)

    all_paths(g, "start", "end")


    # starts = [d for d in dat if "start" in d]
    # ends = [d for d in dat if "end" in d]
    # print("starts:", starts)
    # print("ends:", ends)

    # paths = []
    # start_edge = starts[0]
    # path = [start_edge]
    # remain_edges = dat.copy()
    # remain_edges.remove(start_edge)
    # print(start_edge)
    # print(remain_edges)
    # beg_node = [n for n in start_edge if n != "start"][0]
    # print(beg_node)
    # next_edges = [d for d in remain_edges if beg_node in d]
    # print(next_edges)
    # prev_path = path.copy()
    # new_path = path.copy()
    # for e in next_edges:
    #     new_path.append(e)
    #     print(new_path)

    return len(dat)


def part2(input_file):
    dat = prep_data(input_file)

    return len(dat)


def read_lines(input_file):
    with open(input_file, "r") as fn:
        buf = fn.read()
    return [e.strip() for e in buf.split('\n') if len(e.strip()) > 0]


def prep_data(input_file):
    dat = read_lines(input_file)
    dat = [d.split("-") for d in dat]
    return dat


if __name__ == "__main__":

    # valid_file = "data/12a.txt"
    # valid_file = "data/12b.txt"
    valid_file = "data/12c.txt"
    input_file = "data/12.txt"

    # part 1
    # assert part1(valid_file) == 0
    # print(part1(valid_file))
    # part1(valid_file)
    part1(input_file)
    # assert part1(input_file) == 0
    # print("part 1:", part1(input_file))

    # part 2
    # assert part2(valid_file) == 0
    # print(part2(valid_file))
    # assert part2(input_file) == 0
    # print("part 2:", part2(input_file))
