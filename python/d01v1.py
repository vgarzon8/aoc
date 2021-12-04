# d01v1.py
# Advent of Code 2021 day 1 ver 1
# count of sequence increases
# input: https://adventofcode.com/2021/day/1/input


def part_1(input_file):

    dat = load_data(input_file)
    incr = [dat[k + 1] > dat[k] for k in range(len(dat) - 1)]

    print(len(incr))
    print(incr[:3])
    print(incr[-3:])

    return sum(incr)


def part_2(input_file):

    dat = load_data(input_file)

    win_sum = [sum(dat[slice(k, k + 3)]) for k in range(len(dat) - 2)]

    incr = [win_sum[k + 1] > win_sum[k] for k in range(len(win_sum) - 1)]

    return sum(incr)


def load_data(input_file):

    with open(input_file, "r") as fn:
        buf = fn.read()

    dat = [int(e.strip()) for e in buf.split('\n') if len(e) > 0]

    return dat


if __name__ == "__main__":

    test_input_a = "data/01a.txt"
    input_file = "data/01.txt"

    # part 1
    assert part_1(test_input_a) == 7
    assert part_1(input_file) == 1301

    # part 2
    assert part_2(test_input_a) == 5
    assert part_2(input_file) == 1346
