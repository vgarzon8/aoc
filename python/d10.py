# d08.py
# Advent of Code 2021 day 8 ver 1
# https://adventofcode.com/2021/day/8
# ...


def part1(input_file):
    dat = prep_data(input_file)

    opening = "([{<"
    closing = ")]}>"

    cost = dict(zip(closing, [3, 57, 1197, 25137]))

    cl_match = dict(zip(closing, opening))

    cost_sum = 0
    for k, row in enumerate(dat):
        # print(k, "".join(row))
        op = []
        for d in row:
            if d in opening:
                op.append(d)
                # print(d, "".join(op))
            else:
                c = op.pop()
                if c != cl_match[d]:
                    # print(f"{k} mismatch expecting {c} found {d} cost: {cost[d]}")
                    cost_sum += cost[d]
                    break
                # else:
                #     print(f"{d} closed {c}")

    return cost_sum


def part2(input_file):
    dat = prep_data(input_file)
    opening = "([{<"
    closing = ")]}>"
    cost = dict(zip(closing, [3, 57, 1197, 25137]))
    value = dict(zip(closing, [1, 2, 3, 4]))

    cl_match = dict(zip(closing, opening))
    cl_rev = dict(zip(opening, closing))
    cost_sum = 0
    value_sum = 0
    vals = []
    for k, row in enumerate(dat):
        # print(k, "".join(row))
        skip_rest = False
        op = []
        for d in row:
            if d in opening:
                op.append(d)
                # print(d, "".join(op))
            else:
                c = op.pop()
                if c != cl_match[d]:
                    # print(f"{k} mismatch expecting {c} found {d} cost: {cost[d]}")
                    cost_sum += cost[d]
                    skip_rest = True
                    break
                # else:
                #     print(f"{d} closed {c}")
        if skip_rest:
            continue
        # print(k, "open: ", "".join(op))
        op.reverse()
        cl = [cl_rev[e] for e in op]
        # print("".join(cl))
        value_row = 0
        for e in cl:
            value_row = value_row * 5 + value[e]
        # print(value_row)
        vals.append(value_row)

    vals = sorted(vals)
    score = vals[len(vals) // 2]
    # print(vals, score)

    return score


def read_lines(input_file):
    with open(input_file, "r") as fn:
        buf = fn.read()
    return [e.strip() for e in buf.split('\n') if len(e.strip()) > 0]


def prep_data(input_file):
    dat = read_lines(input_file)
    dat = [list(d) for d in dat]
    return dat


if __name__ == "__main__":

    valid_file = "data/10a.txt"
    input_file = "data/10.txt"

    # # part 1
    assert part1(valid_file) == 26397
    assert part1(input_file) == 344193

    # part 2
    assert part2(valid_file) == 288957
    assert part2(input_file) == 3241238967
