# d13.py
# Advent of Code 2021 day 13 ver 1
# https://adventofcode.com/2021/day/13
# Transparent origami: sequence of folds


def fold(input_file, nfold=None, verbose=False):
    pts, fld = prep_data(input_file)
    xmax = max([x for x, _ in pts])
    ymax = max([y for _, y in pts])
    if verbose:
        print(xmax, ymax)

    grid = {}
    for y in range(ymax + 1):
        for x in range(xmax + 1):
            grid[(x, y)] = 0

    for p in pts:
        grid[(p[0], p[1])] = 1

    # apply folds
    for k, (fold_dir, fold_loc) in enumerate(fld[slice(nfold)]):
        if fold_dir == "y":
            new_xmax = xmax
            if k > 0:
                new_ymax = ymax - fold_loc - 1
            else:
                new_ymax = ymax - fold_loc
            new_grid = {}
            for y in range(new_ymax + 1):
                for x in range(new_xmax + 1):
                    new_grid[(x, y)] = grid[(x, y)]

            for y in range(new_ymax + 1, ymax + 1):
                yref = 2*fold_loc - y
                for x in range(new_xmax + 1):
                    if grid[(x, y)] == 1:
                        new_grid[(x, yref)] = 1

        elif fold_dir == "x":
            if k > 0:
                new_xmax = xmax - fold_loc - 1
            else:
                new_xmax = xmax - fold_loc
            new_ymax = ymax
            new_grid = {}
            for y in range(new_ymax + 1):
                for x in range(new_xmax + 1):
                    new_grid[(x, y)] = grid[(x, y)]

            for x in range(new_xmax + 1, xmax + 1):
                xref = 2*fold_loc - x
                for y in range(new_ymax + 1):
                    if grid[(x, y)] == 1:
                        new_grid[(xref, y)] = 1
        else:
            raise Exception(f"expecting direction x or y, got {fold_dir}")

        if verbose:
            print(k, fold_dir, fold_loc, xmax, ymax, new_xmax, new_ymax)

        grid = new_grid.copy()
        xmax = new_xmax
        ymax = new_ymax

    if verbose:
        print(xmax, ymax)
        for y in range(ymax + 1):
            print("".join(
                ["#" if grid[(x, y)] == 1 else " " for x in range(xmax + 1)]
            ))

    # count active points
    count = sum([
        grid[(x, y)] for y in range(ymax + 1) for x in range(xmax + 1)
    ])
    return count


def read_groups(input_file, sep="\n"):
    with open(input_file, "r") as fn:
        buf = fn.read()
    return [e.strip() for e in buf.split(sep) if len(e.strip()) > 0]


def prep_data(input_file):
    grp = read_groups(input_file, sep="\n\n")
    pts = [tuple(map(int, t.split(","))) for t in grp[0].split("\n")]
    fld = [t.split("fold along ")[1].split("=") for t in grp[1].split("\n")]
    fld = [(t[0], int(t[1])) for t in fld]
    return pts, fld


if __name__ == "__main__":

    valid_file = "data/13a.txt"
    input_file = "data/13.txt"

    # part 1
    assert fold(valid_file, 1, True) == 17
    assert fold(input_file, 1) == 795

    # part 2
    assert fold(valid_file, verbose=True) == 16
    assert fold(input_file, verbose=True) == 88
