# dXXv1.py
# Advent of Code 2021 day XX ver 1
# count of sequence increases
# input: https://adventofcode.com/2021/day/XX/input


def part_1(input_file):

    dat = load_data(input_file)

    return len(dat)


def part_2(input_file):

    dat = load_data(input_file)

    return len(dat)


def load_data(input_file):

    with open(input_file, "r") as fn:
        buf = fn.read()

    dat = [e.strip() for e in buf.split('\n') if len(e.strip()) > 0]

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
