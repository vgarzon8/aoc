# d04v1.py


def part_1(input_file):

    seq, boards = load_data(input_file)

    # board as a map
    boards_map = {}
    for k, b in enumerate(boards):
        for _, e in enumerate(b):
            boards_map[(k, e[0], e[1])] = e[2]

    # initialize state
    state = {}
    for k, b in enumerate(boards):
        for _, e in enumerate(b):
            state[(k, e[0], e[1])] = False

    nrows = 5
    ncols = 5

    rows = {}
    cols = {}
    for k, b in enumerate(boards):
        for r in range(nrows):
            rows[(k, r)] = [state[(k, r, c)] for c in range(ncols)]
        for c in range(ncols):
            cols[(k, c)] = [state[(k, r, c)] for r in range(nrows)]

    bingo = False
    for d in seq:
        for k, b in enumerate(boards):
            for e in b:
                if d == e[2]:
                    state[(k, e[0], e[1])] = True

        for k, b in enumerate(boards):
            for r in range(nrows):
                rows[(k, r)] = [state[(k, r, c)] for c in range(ncols)]
            for c in range(ncols):
                cols[(k, c)] = [state[(k, r, c)] for r in range(nrows)]

        for (k, r) in rows.keys():
            if all(rows[(k, r)]):
                bingo = True
                print(f"bingo num {d} board {k} row {r}")
                break

        for (k, c) in cols.keys():
            if all(cols[(k, c)]):
                bingo = True
                print(f"bingo num {d} board {k} col {c}")
                break

        if bingo:
            break

    if bingo:
        unmarked = 0
        for r in range(nrows):
            for c in range(ncols):
                if state[(k, r, c)] is False:
                    unmarked += boards_map[(k, r, c)]

    return unmarked * d


def part_2(input_file):

    seq, boards = load_data(input_file)

    # board as a map
    boards_map = {}
    for k, b in enumerate(boards):
        for _, e in enumerate(b):
            boards_map[(k, e[0], e[1])] = e[2]

    # initialize state
    state = {}
    for k, b in enumerate(boards):
        for _, e in enumerate(b):
            state[(k, e[0], e[1])] = False

    nrows = 5
    ncols = 5

    rows = {}
    cols = {}
    for k in range(len(boards)):
        for r in range(nrows):
            rows[(k, r)] = [state[(k, r, c)] for c in range(ncols)]
        for c in range(ncols):
            cols[(k, c)] = [state[(k, r, c)] for r in range(nrows)]

    board_state = [False for _ in range(len(boards))]

    for i, d in enumerate(seq):
        for k, b in enumerate(boards):
            for e in b:
                if d == e[2]:
                    state[(k, e[0], e[1])] = True

        # update board state
        for k, _ in enumerate(boards):
            for r in range(nrows):
                rows[(k, r)] = [state[(k, r, c)] for c in range(ncols)]
            for c in range(ncols):
                cols[(k, c)] = [state[(k, r, c)] for r in range(nrows)]

        for (k, r) in rows.keys():
            if all(rows[(k, r)]):
                if board_state[k] is True:
                    continue
                board_state[k] = True
                print(f"{sum(board_state)} iter {i} num {d} board {k} row {r}")
                if all(board_state):
                    break

        if all(board_state):
            break

        for (k, c) in cols.keys():
            if all(cols[(k, c)]):
                if board_state[k] is True:
                    continue
                board_state[k] = True
                print(f"{sum(board_state)} iter {i} num {d} board {k} col {c}")
                if all(board_state):
                    break

        if all(board_state):
            break

    if all(board_state):
        unmarked = 0
        for r in range(nrows):
            for c in range(ncols):
                if state[(k, r, c)] is False:
                    unmarked += boards_map[(k, r, c)]

    return unmarked * d


def load_data(input_file):

    with open(input_file, "r") as fn:
        buf = fn.read()

    lines = [e.strip() for e in buf.split('\n\n') if len(e.strip()) > 0]

    seq = list(map(int, lines[0].split(',')))

    boards = []
    for g in lines[1:]:
        rows = [list(map(int, r.split())) for r in g.split("\n")]
        b = []
        for j, r in enumerate(rows):
            for i, e in enumerate(r):
                b.append((i, j, e))
        boards.append(b)

    return seq, boards


if __name__ == "__main__":

    test_input_a = "data/04a.txt"
    input_file = "data/04.txt"

    # part 1
    assert part_1(test_input_a) == 4512
    assert part_1(input_file) == 27027

    # part 2
    assert part_2(test_input_a) == 1924
    assert part_2(input_file) == 36975
