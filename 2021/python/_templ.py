# d15.py
# Advent of Code 2021 day 15 ver 1
# https://adventofcode.com/2021/day/15
# ...


def part1(input_file):
    dat = prep_data(input_file)

    return len(dat)


def part2(input_file):
    dat = prep_data(input_file)

    return len(dat)


def read_groups(input_file, sep="\n"):
    with open(input_file, "r") as fn:
        buf = fn.read()
    return [e.strip() for e in buf.split(sep) if len(e.strip()) > 0]


def prep_data(input_file):
    dat = read_groups(input_file)
    # dat = ...
    return dat


if __name__ == "__main__":

    valid_file = "data/15a.txt"
    input_file = "data/15.txt"

    # part 1
    print(part1(valid_file))
    # print("part 1:", part1(input_file))
    # assert part1(valid_file) == 0
    # assert part1(input_file) == 0

    # part 2
    # print(part2(valid_file))
    # print("part 2:", part2(input_file))
    # assert part2(valid_file) == 0
    # assert part2(input_file) == 0
