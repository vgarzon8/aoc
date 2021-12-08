# d08.py
# Advent of Code 2021 day 8 ver 1
# https://adventofcode.com/2021/day/8
# ...


def part1(input_file):
    dat = prep_data(input_file)

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
    # dat = ...
    return dat


if __name__ == "__main__":

    valid_file = "data/08a.txt"
    input_file = "data/08.txt"

    # part 1
    # assert part1(valid_file) == 0
    print(part1(valid_file))
    # assert part1(input_file) == 0
    # print("part 1:", part1(input_file))

    # part 2
    # assert part2(valid_file) == 0
    # print(part2(valid_file))
    # assert part1(input_file) == 0
    # print("part 2:", part2(input_file))
