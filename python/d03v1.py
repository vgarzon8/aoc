# d03v1.py
# Advent of Code 2021 day 3 ver 1
# count of sequence increases
# input: https://adventofcode.com/2021/day/3/input

import copy


def part_1(input_file):

    dat = load_data(input_file)
    size = len(dat)

    c = [(1 if sum(e) > (size // 2) else 0) for e in map(list, zip(*dat))]
    s = "".join([str(i) for i in c])
    gam = int(s, 2)
    print(s, gam)

    c = [(0 if sum(e) > (size // 2) else 1) for e in map(list, zip(*dat))]
    s = "".join([str(i) for i in c])
    eps = int(s, 2)
    print(s, eps)

    return gam * eps


def part_2(input_file):

    dat = load_data(input_file)
    buf = copy.deepcopy(dat)

    for pos in range(len(buf[0])):
        s = len(buf)
        g = [(1 if (sum(e) / s) >= 0.5 else 0) for e in map(list, zip(*buf))]
        buf = [e for e in buf if e[pos] == g[pos]]
        print(pos, len(buf))

    print(buf)
    s = "".join([str(i) for i in buf[0]])
    oxy = int(s, 2)
    print(s, oxy)

    buf = copy.deepcopy(dat)

    for pos in range(len(buf[0])):
        s = len(buf)
        g = [(0 if (sum(e) / s) >= 0.5 else 1) for e in map(list, zip(*buf))]
        buf = [e for e in buf if e[pos] == g[pos]]
        print(pos, len(buf))
        if len(buf) == 1:
            break

    print(buf)
    s = "".join([str(i) for i in buf[0]])
    co2 = int(s, 2)
    print(s, co2)

    print(oxy, co2)

    return oxy * co2


def load_data(input_file):

    with open(input_file, "r") as fn:
        buf = fn.read()

    dat = [
        list(map(int, e.strip()))
        for e in buf.split('\n') if len(e.strip()) > 0
    ]

    return dat


if __name__ == "__main__":

    test_input_a = "data/03a.txt"
    input_file = "data/03.txt"

    assert part_1(test_input_a) == 198
    assert part_1(input_file) == 749376

    # assert part_1(test_input_a) == 230
    print(part_1(test_input_a))
    assert part_2(input_file) == 2372923
