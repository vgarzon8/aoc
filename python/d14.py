# d14.py
# Advent of Code 2021 day 14 ver 1
# https://adventofcode.com/2021/day/11
# Extended poly

from collections import Counter


def part1(input_file, nsteps=10):
    tmplt, rules = prep_data(input_file)
    rules = {k: v for (k, v) in rules}
    print(tmplt)
    print(len(rules))

    for t in range(nsteps):
        poly = []
        for k in range(len(tmplt) - 1):
            srch_pair = "".join(tmplt[slice(k, k + 2)])
            insert = rules.get(srch_pair, None)
            poly.append(tmplt[k])
            if insert is not None:
                poly.append(insert)
        poly.append(tmplt[-1])

        tmplt = poly.copy()

    cntr = Counter(tmplt)

    count = cntr.most_common(None)
    max_count = max(count, key=lambda x: x[1])[1]
    min_count = min(count, key=lambda x: x[1])[1]

    print(count)

    return max_count - min_count


def part2(input_file, nsteps=10):
    tmplt, rules = prep_data(input_file)
    rules = {k: v for (k, v) in rules}
    print(tmplt)
    print(len(rules))

    pair_count = {}
    for k in range(len(tmplt) - 1):
        p = "".join(tmplt[slice(k, k + 2)])
        pair_count[p] = pair_count.get(p, 0) + 1

    for t in range(nsteps):
        pair_split = {}
        for k, v in pair_count.items():
            insert = rules.get(k, None)
            if insert is not None:
                left = k[0] + insert
                right = insert + k[1]
                pair_split[left] = pair_split.get(left, 0) + v
                pair_split[right] = pair_split.get(right, 0) + v

        pair_count = pair_split.copy()

    elem_count = {}
    for k, v in pair_count.items():
        elem_count[k[0]] = elem_count.get(k[0], 0) + v
    elem_count[tmplt[-1]] = elem_count.get(tmplt[-1], 0) + 1

    print(pair_split)
    print(elem_count)

    count = tuple(elem_count.items())
    max_count = max(count, key=lambda x: x[1])[1]
    min_count = min(count, key=lambda x: x[1])[1]
    print(max_count, min_count, max_count - min_count)

    return max_count - min_count


def read_groups(input_file, sep='\n'):
    with open(input_file, "r") as fn:
        buf = fn.read()
    return [e.strip() for e in buf.split(sep) if len(e.strip()) > 0]


def prep_data(input_file):
    grp = read_groups(input_file, "\n\n")
    tmplt = list(grp[0])
    rules = [tuple(t.split(" -> ")) for t in grp[1].split("\n")]
    return tmplt, rules


if __name__ == "__main__":

    valid_file = "data/14a.txt"
    input_file = "data/14.txt"

    # part 1
    assert part1(valid_file) == 1588
    assert part1(input_file) == 3095

    # part 2
    assert part2(valid_file, 40) == 2188189693529
    assert part2(input_file, 40) == 3152788426516
