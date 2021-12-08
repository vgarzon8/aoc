# d08.py
# Advent of Code 2021 day 8 ver 1
# https://adventofcode.com/2021/day/8
# ...

# display segments by number (arranged by count)
# segments: 0: top, 1: upper left, 2: upper right, 3: middle
#   4: lower left, 5: lower right, 6: bottom
DISP = {
    1: [2, 5],
    7: [0, 2, 5],
    4: [1, 2, 3, 5],
    2: [0, 2, 3, 4, 6],
    3: [0, 2, 3, 5, 6],
    5: [0, 1, 3, 5, 6],
    6: [0, 1, 3, 4, 5, 6],
    0: [0, 1, 2, 4, 5, 6],
    9: [0, 1, 2, 3, 5, 6],
    8: [0, 1, 2, 3, 4, 5, 6],
}
disp_rev = {tuple(v): k for k, v in DISP.items()}


def part1(input_file):
    num_sgm = {1: 2, 4: 4, 7: 3, 8: 7}
    dat = prep_data(input_file)

    cnt = 0
    for (sig, out) in dat:
        o = [len(set(t)) for t in out]
        for e in o:
            if e in num_sgm.values():
                cnt += 1

    return cnt


def part2(input_file):
    return sum([decode(s, o) for s, o in prep_data(input_file)])


def decode(sig, out):

    # split words and group by count
    sig_cnt = {c: [list(s) for s in sig if len(s) == c] for c in range(2, 8)}

    # check word length counts
    idx_req = {2: 1, 3: 1, 4: 1, 5: 3, 6: 3, 7: 1}
    for k, v in sig_cnt.items():
        assert len(v) == idx_req[k]

    # segment 0 (top) is difference between words of count 3 and 2
    sgm = {}
    sgm[0] = diff_single(sig_cnt[3][0], sig_cnt[2][0])

    # to identify segments 1 (upper left) and 4 (lower left):
    # count all letters in words of length 5
    cnt_5 = {}
    for c in [e for s in sig_cnt[5] for e in s]:
        cnt_5[c] = cnt_5.get(c, 0) + 1

    # segment 1 is single occurrence of len 5 that also appears in len 4
    cnt_5_1 = [k for k, v in cnt_5.items() if v == 1]
    sgm[1] = inter_single(cnt_5_1, sig_cnt[4][0])

    # segment 4 is the other single occurrence in words of len 5
    sgm[4] = diff_single(cnt_5_1, sgm.values())

    # segment 3 (middle) is element w/o assignment in set difference between
    # words of size 4 and size 2
    sgm[3] = diff_single(ldiff(sig_cnt[4][0], sig_cnt[2][0]), [sgm[1]])

    # segment 6 (bottom) is common elem in words of size 5, not yet assigned
    tmp = linter(linter(sig_cnt[5][0], sig_cnt[5][1]), sig_cnt[5][2])
    sgm[6] = diff_single(tmp, sgm.values())

    # segment 5 (lower right) is common elem in words of size 6, n / y / a
    tmp = linter(linter(sig_cnt[6][0], sig_cnt[6][1]), sig_cnt[6][2])
    sgm[5] = diff_single(tmp, sgm.values())

    # segment 2 (upper right) is remainder in word of size 7
    sgm[2] = diff_single(sig_cnt[7][0], sgm.values())

    # decode words
    rev = {v: k for (k, v) in sgm.items()}
    n = [disp_rev[tuple(sorted([rev[c] for c in list(o)]))] for o in out]

    return int("".join([str(i) for i in n]))


def diff_single(a, b):
    e = ldiff(a, b)
    assert len(e) == 1
    return e[0]


def inter_single(a, b):
    e = linter(a, b)
    assert len(e) == 1
    return e[0]


def ldiff(x, y):
    return [i for i in x if i not in y]


def linter(x, y):
    return [i for i in x if i in y]


def read_lines(input_file):
    with open(input_file, "r") as fn:
        buf = fn.read()
    return [e.strip() for e in buf.split('\n') if len(e.strip()) > 0]


def prep_data(input_file):
    dat = read_lines(input_file)
    dat = [d.split("|") for d in dat]
    dat = [(e[0].split(), e[1].split()) for e in dat]
    return dat


if __name__ == "__main__":

    valid_file = "data/08a.txt"
    input_file = "data/08.txt"

    # part 1
    assert part1(valid_file) == 26
    assert part1(input_file) == 530

    # part 2
    assert part2(valid_file) == 61229
    assert part2(input_file) == 1051087
