# d06.py
# Advent of Code 2021 day 6 ver 1
# https://adventofcode.com/2021/day/6
# ...

import copy


def count_state(input_file, days=80):
    dat = prep_data(input_file)
    cnt = {k: 0 for k in range(9)}
    for d in dat:
        cnt[d] += 1
    for t in range(days):
        new = {}
        for k in range(8):
            new[k] = cnt[k + 1]
        new[8] = cnt[0]
        new[6] += cnt[0]
        cnt = new
    return sum(cnt.values())


def pop_state(input_file, days=80):
    dat = prep_data(input_file)
    for t in range(days):
        new = copy.copy(dat)
        for k, d in enumerate(dat):
            if d > 0:
                new[k] -= 1
            else:
                new[k] = 6
                new.append(8)
        dat = new
    return len(dat)


def read_lines(input_file):
    with open(input_file, "r") as fn:
        buf = fn.read()
    return [e.strip() for e in buf.split('\n') if len(e.strip()) > 0]


def prep_data(input_file):
    dat = read_lines(input_file)
    dat = list(map(int, [e.strip() for e in dat[0].split(',')]))
    return dat


if __name__ == "__main__":

    test_input_a = "data/06a.txt"
    input_file = "data/06.txt"

    # part 1 - using population
    assert pop_state(test_input_a) == 5934
    assert pop_state(input_file) == 386640

    # part 1 - updating counts
    assert count_state(test_input_a) == 5934
    assert count_state(input_file) == 386640

    # part 2
    assert count_state(test_input_a, days=256) == 26984457539
    assert count_state(input_file, days=256) == 1733403626279
