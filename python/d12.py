# d12.py
# Advent of Code 2021 day 12 ver 1
# https://adventofcode.com/2021/day/12
# Passage paths

import networkx as nx


class Graph:
    def __init__(self, dat):
        self.g = nx.Graph(dat)
        self.paths = []

    def all_paths_part1(self, current, end, visited, path):
        visited[current] = True
        path.append(current)

        if current == end:
            self.paths.append(path.copy())
        else:
            for i in self.g[current]:
                if visited[i] is False or i.isupper():
                    self.all_paths_part1(i, end, visited, path)

        path.pop()
        visited[current] = False

    def all_paths_part2(self, current, end, visited, path, count):
        visited[current] = True
        count[current] += 1
        path.append(current)

        if current == end:
            if path not in self.paths:
                self.paths.append(path.copy())
        else:
            for i in self.g[current]:
                cnt = [
                    c for (k, c) in count.items()
                    if (k.islower() and k != "start" and k != "end")
                ]
                mask = (
                    visited[i] is False or i.isupper() is True
                    or (
                        i != "start"
                        and i.islower()
                        and all([c <= 2 for c in cnt])
                        and (len([c for c in cnt if c > 1]) < 2)
                    )
                )
                if mask:
                    self.all_paths_part2(i, end, visited, path, count)
 
        path.pop()
        visited[current] = False
        count[current] -= 1

    def all_paths(self, start, end, mode="part1"):
        visited = {}
        for k in self.g.nodes:
            visited[k] = False

        count = {}
        for k in self.g.nodes:
            count[k] = 0

        path = []
        if mode == "part1":
            self.all_paths_part1(start, end, visited, path)
        elif mode == "part2":
            self.all_paths_part2(start, end, visited, path, count)
        else:
            raise Exception(
                f"mode should be one of 'part1' or 'part'2, got {mode}"
            )

        return self.paths


def count_paths(input_file, mode="part1", verbose=False):
    caves = Graph(prep_data(input_file))
    paths = caves.all_paths("start", "end", mode=mode)

    if verbose is True:
        print(caves.g)
        print("nodes", caves.g.nodes)
        print("edges", caves.g.edges)
        for p in paths:
            print(p)

    return len(paths)


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
    input_file = "data/12.txt"

    # # part 1
    # assert count_paths(valid_file) == 10
    # assert count_paths(input_file) == 3450

    # # part 2
    print(count_paths(valid_file, "part2", True))
