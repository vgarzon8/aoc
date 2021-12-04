# d02v1.py
# Advent of Code 2021 day 2 ver 1
# count of sequence increases
# input: https://adventofcode.com/2021/day/2/input


def part_1(input_file):

    dat = load_data(input_file)
    print(dat[-5:])

    x, y = 0, 0
    for action, size in dat:
        size = int(size)
        if action == "forward":
            x += size
        elif action == "down":
            y += size
        elif action == "up":
            y -= size
        else:
            raise Exception("unrecognized action")

    print(x, y)

    return x * y


def part_2(input_file):

    dat = load_data(input_file)

    x, y, aim = 0, 0, 0
    for action, size in dat:
        size = int(size)
        if action == "forward":
            x += size
            y += aim * size
        elif action == "down":
            aim += size
        elif action == "up":
            aim -= size
        else:
            raise Exception("unrecognized action")

    print(x, y, aim)

    return x * y


def load_data(input_file):

    with open(input_file, "r") as fn:
        buf = fn.read()

    dat = [e.strip().split() for e in buf.split('\n') if len(e.strip()) > 0]

    return dat


if __name__ == "__main__":

    test_input_a = "data/02a.txt"
    input_file = "data/02.txt"

    # part 1
    assert part_1(test_input_a) == 150
    assert part_1(input_file) == 1924923

    # part 2
    assert part_2(test_input_a) == 900
    assert part_2(input_file) == 1982495697
