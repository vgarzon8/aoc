# dxx.py
# Advent of Code 2021 day XX ver 1
# https://adventofcode.com/2021/day/xx
# count of sequence increases


def part_1(input_file):

    dat = prep_data(input_file)

    return len(dat)


def part_2(input_file):

    dat = prep_data(input_file)

    return len(dat)


def read_lines(input_file):
    with open(input_file, "r") as fn:
        buf = fn.read()
    return [e.strip() for e in buf.split('\n') if len(e.strip()) > 0]


def prep_data(input_file):
    dat = read_lines(input_file)
    # additional processing
    # dat = ...
    return dat


if __name__ == "__main__":

    test_input_a = "data/01a.txt"
    input_file = "data/01.txt"

    # part 1
    assert part_1(test_input_a) == 10
    ans = part_1(input_file)
    print("part 1:", ans)
    # ans: 2000

    # part 2
    assert part_2(test_input_a) == 10
    ans = part_2(input_file)
    print("part 2:", ans)
    # ans: 2000
