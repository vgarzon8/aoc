# d05.py
# Advent of Code 2021 day 05 ver 1
# https://adventofcode.com/2021/day/5
# Hydrothermal venture, map with overlapping lines


def part_1(input_file):
    dat = prep_data(input_file)

    xmax = max([max([p[0][0], p[1][0]]) for p in dat]) + 1
    ymax = max([max([p[0][1], p[1][1]]) for p in dat]) + 1

    print(xmax, ymax)

    grid = {(i, j): 0 for j in range(ymax) for i in range(xmax)}

    for k, (beg, end) in enumerate(dat):
        if beg[0] == end[0]:
            if beg[1] < end[1]:
                r = range(beg[1], end[1] + 1)
            else:
                r = range(end[1], beg[1] + 1)
            for j in r:
                grid[(beg[0], j)] += 1

        elif beg[1] == end[1]:
            if beg[0] < end[0]:
                r = range(beg[0], end[0] + 1)
            else:
                r = range(end[0], beg[0] + 1)
            for i in r:
                grid[(i, beg[1])] += 1

    # for j in range(ymax):
    #     print("".join([str(grid[(i, j)]) for i in range(xmax)]))

    count = sum([
        1 if grid[(i, j)] > 1 else 0
        for j in range(ymax) for i in range(xmax)
    ])

    return count


def part_2(input_file):
    dat = prep_data(input_file)

    xmax = max([max([p[0][0], p[1][0]]) for p in dat]) + 1
    ymax = max([max([p[0][1], p[1][1]]) for p in dat]) + 1

    grid = {(i, j): 0 for j in range(ymax) for i in range(xmax)}

    for k, (beg, end) in enumerate(dat):
        if beg[0] == end[0]:
            if beg[1] < end[1]:
                r = range(beg[1], end[1] + 1)
            else:
                r = range(end[1], beg[1] + 1)
            for j in r:
                grid[(beg[0], j)] += 1

        elif beg[1] == end[1]:
            if beg[0] < end[0]:
                r = range(beg[0], end[0] + 1)
            else:
                r = range(end[0], beg[0] + 1)
            for i in r:
                grid[(i, beg[1])] += 1

        else:
            length = abs(end[0] - beg[0]) + 1
            for k in range(length):
                if beg[0] < end[0]:
                    x = beg[0] + k
                else:
                    x = end[0] + k
                m = (end[1] - beg[1]) / (end[0] - beg[0])
                y = m * (x - beg[0]) + beg[1]
                grid[(x, y)] += 1

    # for j in range(ymax):
    #     print("".join([str(grid[(i, j)]) for i in range(xmax)]))

    count = sum([
        1 if grid[(i, j)] > 1 else 0
        for j in range(ymax) for i in range(xmax)
    ])

    return count


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

    # part 1
    assert part_1(test_input_a) == 5
    assert part_1(input_file) == 5632

    # part 2
    assert part_2(test_input_a) == 12
    assert part_2(input_file) == 22213
