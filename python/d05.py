# d05.py
# Advent of Code 2021 day 05 ver 1
# https://adventofcode.com/2021/day/5
# Hydrothermal venture, map with overlapping lines

class Map:
    def __init__(self, dat):
        self.dat = dat
        self.xmax = max([max([p[0][0], p[1][0]]) for p in dat]) + 1
        self.ymax = max([max([p[0][1], p[1][1]]) for p in dat]) + 1
        self.grid = {
            (i, j): 0 for j in range(self.ymax) for i in range(self.xmax)
        }

    def update_up_down(self):
        for k, (beg, end) in enumerate(self.dat):
            if beg[0] == end[0]:
                if beg[1] < end[1]:
                    r = range(beg[1], end[1] + 1)
                else:
                    r = range(end[1], beg[1] + 1)
                for j in r:
                    self.grid[(beg[0], j)] += 1

            elif beg[1] == end[1]:
                if beg[0] < end[0]:
                    r = range(beg[0], end[0] + 1)
                else:
                    r = range(end[0], beg[0] + 1)
                for i in r:
                    self.grid[(i, beg[1])] += 1

    def update_diag(self):
        for k, (beg, end) in enumerate(self.dat):
            if beg[0] == end[0] or beg[1] == end[1]:
                continue
            length = abs(end[0] - beg[0]) + 1
            for k in range(length):
                if beg[0] < end[0]:
                    x = beg[0] + k
                else:
                    x = end[0] + k
                m = (end[1] - beg[1]) / (end[0] - beg[0])
                y = m * (x - beg[0]) + beg[1]
                self.grid[(x, y)] += 1

    def count_overlaps(self):
        return sum([
            1 if self.grid[(i, j)] > 1 else 0
            for j in range(self.ymax) for i in range(self.xmax)
        ])

    def print_state(self):
        for j in range(self.ymax):
            print("".join([str(self.grid[(i, j)]) for i in range(self.xmax)]))


def part_1(input_file, debug=False):
    dat = prep_data(input_file)
    g = Map(dat)
    g.update_up_down()
    if debug:
        g.print_state()
    return g.count_overlaps()


def part_2(input_file, debug=False):
    dat = prep_data(input_file)
    g = Map(dat)
    g.update_up_down()
    g.update_diag()
    if debug:
        g.print_state()

    return g.count_overlaps()


def read_lines(input_file):
    with open(input_file, "r") as fn:
        buf = fn.read()
    return [e.strip() for e in buf.split('\n') if len(e.strip()) > 0]


def prep_data(input_file):
    dat = read_lines(input_file)
    dat = [e.split("->") for e in dat]
    dat = [tuple(map(int, f.split(','))) for s in dat for f in s]
    dat = list(zip(dat[::2], dat[1::2]))
    return dat


if __name__ == "__main__":

    test_input_a = "data/05a.txt"
    input_file = "data/05.txt"

    assert part_1(test_input_a, debug=True) == 5
    assert part_1(input_file) == 5632

    assert part_2(test_input_a, debug=True) == 12
    assert part_2(input_file) == 22213
