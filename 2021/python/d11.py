# d11.py
# Advent of Code 2021 day 11 ver 1
# https://adventofcode.com/2021/day/11
# Dumbo octopus: count flashes and first instance when all flash

def iterate(input_file, niter=1000, all_flash=False):
    dat = prep_data(input_file)
    # number of rows and columns (assumes fixed width)
    nri = len(dat)
    nci = len(dat[0])

    # load data into grid indexed by tupples
    grid = {(i, j): int(dat[j][i]) for j in range(nri) for i in range(nci)}

    # neighbors
    nb = [(i, j) for i in range(-1, 2) for j in range(-1, 2)]
    nb.remove((0, 0))

    print("initial state")
    for j in range(nri):
        print("".join([str(grid[(i, j)]) for i in range(nci)]))

    flash_cnt = 0
    for t in range(niter):
        # step update
        for j in range(nri):
            for i in range(nci):
                grid[(i, j)] += 1

        lit = []  # flashed
        lit_old = []  # previous pass
        # update neighbors
        for u in range(nri * nci):
            for j in range(nri):
                for i in range(nci):
                    if grid[(i, j)] > 9:
                        if (i, j) in lit:
                            continue
                        else:
                            lit.append((i, j))
                        # visit each neibhbor
                        for k in nb:
                            x = i + k[0]
                            y = j + k[1]
                            if x < 0 or x >= nci or y < 0 or y >= nri:
                                continue
                            grid[(x, y)] += 1

            if lit == lit_old:
                # print(f"{t} {u} {len(lit)} ")
                break
            else:
                lit_old = lit.copy()

        # reset count after flash
        for j in range(nri):
            for i in range(nci):
                if grid[(i, j)] > 9:
                    grid[(i, j)] = 0

        # aupdate flash count
        flash_cnt += len(lit)

        # stop if all flashed and mode is all_flash
        if len(lit) == nri * nci and all_flash:
            break

    print("final state")
    for j in range(nri):
        print("".join([str(grid[(i, j)]) for i in range(nci)]))

    # return flash count and step number
    return flash_cnt, t + 1


def read_lines(input_file):
    with open(input_file, "r") as fn:
        buf = fn.read()
    return [e.strip() for e in buf.split('\n') if len(e.strip()) > 0]


def prep_data(input_file):
    dat = read_lines(input_file)
    return dat


if __name__ == "__main__":

    valid_file = "data/11a.txt"
    input_file = "data/11.txt"

    # # part 1
    assert iterate(valid_file, niter=100)[0] == 1656
    assert iterate(input_file, niter=100)[0] == 1588

    # part 2
    assert iterate(valid_file, all_flash=True)[1] == 195
    assert iterate(input_file, all_flash=True)[1] == 517
