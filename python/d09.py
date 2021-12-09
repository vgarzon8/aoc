# d09.py
# Advent of Code 2021 day 9 ver 1
# https://adventofcode.com/2021/day/8
# Smoke basin: Find low points and basins

# neighbor increments
NEIGH = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def part1(input_file, debug=False):
    grid, nri, nci = setup_grid(prep_data(input_file))
    if debug:
        print_grid(grid, nri, nci)
    low_loc = find_low(grid, nri, nci)
    return sum([grid[(p[0], p[1])] + 1 for p in low_loc])


def part2(input_file):
    grid, nri, nci = setup_grid(prep_data(input_file))
    low_loc = find_low(grid, nri, nci)

    basin_sizes = []
    # checked = []  # assumes non-overlapping basins
    for seed_loc in low_loc:
        seed_val = grid[(seed_loc[0], seed_loc[1])]
        basin = []
        basin.append(seed_val)
        srch = []
        srch.append(seed_loc)
        checked = []  # allows overlapping basins
        checked.append(seed_loc)

        while len(srch) > 0:
            (i, j) = srch.pop()
            for step in NEIGH:
                nloc = (i + step[0], j + step[1])
                n = grid[nloc]
                if n < 9 and nloc not in checked:
                    basin.append(n)
                    checked.append(nloc)
                    srch.append(nloc)
        basin_sizes.append(len(basin))

    largest = sorted(basin_sizes, reverse=True)[:3]
    return largest[0] * largest[1] * largest[2]


def setup_grid(dat):
    # interior size
    nri = len(dat)
    nci = len(dat[0])

    # fill-in interior points
    grid = {}
    for j, row in enumerate(dat):
        for i, c in enumerate(row):
            grid[(i + 1, j + 1)] = int(c)

    # boundary padding
    for j in range(nri + 2):
        grid[(0, j)] = 9
        grid[(nci + 1, j)] = 9

    for i in range(nci + 2):
        grid[(i, 0)] = 9
        grid[(i, nri + 1)] = 9

    return grid, nri, nci


def find_low(grid, nri, nci):
    low_loc = []
    for j in range(1, nri + 1):
        for i in range(1, nci + 1):
            c = 0
            for n in NEIGH:
                if grid[(i + n[0], j + n[1])] > grid[(i, j)]:
                    c += 1
            if c == 4:
                low_loc.append((i, j))
    return low_loc


def print_grid(grid, nri, nci):
    for j in range(nri + 2):
        print("".join([str(grid[(i, j)]) for i in range(nci + 2)]))


def read_lines(input_file):
    with open(input_file, "r") as fn:
        buf = fn.read()
    return [e.strip() for e in buf.split('\n') if len(e.strip()) > 0]


def prep_data(input_file):
    dat = read_lines(input_file)
    return dat


if __name__ == "__main__":

    valid_file = "data/09a.txt"
    input_file = "data/09.txt"

    # # part 1
    assert part1(valid_file, debug=True) == 15
    assert part1(input_file) == 585

    # part 2
    assert part2(valid_file) == 1134
    assert part2(input_file) == 827904
