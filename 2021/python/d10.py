# d08.py
# Advent of Code 2021 day 8 ver 1
# https://adventofcode.com/2021/day/8
# Syntax scoring: matching groups

from functools import reduce


def syntax_score(input_file):
    opening, closing = "([{<", ")]}>"
    cost = dict(zip(closing, [3, 57, 1197, 25137]))
    value = dict(zip(closing, [1, 2, 3, 4]))
    cl_match = dict(zip(closing, opening))
    cl_rev = dict(zip(opening, closing))
    cost_sum = 0
    vals = []
    for k, row in enumerate(prep_data(input_file)):
        # print(k, "".join(row))
        skip_rest = False
        op = []
        for d in row:
            if d in opening:
                op.append(d)
            else:
                c = op.pop()
                if c != cl_match[d]:
                    # print(f"{k} expecting {c} found {d} cost: {cost[d]}")
                    cost_sum += cost[d]
                    skip_rest = True
                    break
                # else:
                #     print(f"{d} closed {c}")
        if skip_rest:
            continue
        cl = [cl_rev[e] for e in op[::-1]]
        # print("".join(op), "".join(cl))
        value_row = reduce(lambda a, b: 5*a + value[b], cl, 0)
        vals.append(value_row)

    vals = sorted(vals)
    score = vals[len(vals) // 2]

    return cost_sum, score


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

    assert syntax_score(valid_file) == (26397, 288957)
    assert syntax_score(input_file) == (344193, 3241238967)
