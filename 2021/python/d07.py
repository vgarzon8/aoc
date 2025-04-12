# d07.py
# Advent of Code 2021 day 7 ver 1
# https://adventofcode.com/2021/day/7
# Treachery of whales: find optimal number of steps


def part1(input_file):
    dat = prep_data(input_file)
    fmin = len(dat)*max(dat)**2
    for i in range(max(dat)):
        fuel = sum([abs(t - i) for t in dat])
        fmin = min(fmin, fuel)

    return fmin


def part2(input_file):
    dat = prep_data(input_file)

    def recur_sum(n):
        return int((n + 1) * n / 2)

    fmin = len(dat)*max(dat)**2
    for i in range(max(dat)):
        fuel = sum([recur_sum(abs(t - i + 1)) for t in dat])
        fmin = min(fmin, fuel)

    return fmin


def read_lines(input_file):
    with open(input_file, "r") as fn:
        buf = fn.read()
    return [e.strip() for e in buf.split('\n') if len(e.strip()) > 0]


def prep_data(input_file):
    dat = read_lines(input_file)
    dat = list(map(int, dat[0].split(",")))
    return dat


if __name__ == "__main__":

    # validation and input files
    valid_file = "data/07a.txt"
    input_file = "data/07.txt"

    # part 1
    assert part1(valid_file) == 37
    assert part1(input_file) == 337833

    # part 2
    assert part2(valid_file) == 168
    assert part2(input_file) == 96678050
