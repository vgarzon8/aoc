# d17.py
# Advent of Code 2021 day 17 ver 1
# https://adventofcode.com/2021/day/17
# Trick shot


def find_ymax(input_file, vy_lims=(-1000, 1000), vx_max=200, tmax=1000):
    dat = prep_data(input_file)
    xt = tuple(sorted(dat[0:2]))
    yt = tuple(sorted(dat[2:4]))
    # print(xt, yt)

    res = []
    for vy in range(*vy_lims):
        for vx in range(1, vx_max):
            # print(vx, vy)
            ym, x, y, t = launch_probe(vx, vy, xt, yt, tmax=tmax)

            if ym is not None:
                res.append((vx, vy, ym))

    best_res = max(res, key=lambda x: x[2])
    print(best_res, len(set(res)))
    ymax = best_res[2]

    return ymax, len(set(res))


def launch_probe(vx, vy, xt, yt, tmax=1000, x=0, y=0):
    ymax = y
    hit_target = False
    for t in range(tmax):
        x += vx
        y += vy
        # print(x, y, vx, vy)
        ymax = max(y, ymax)
        if x >= xt[0] and x <= xt[1] and y >= yt[0] and y <= yt[1]:
            hit_target = True
            break
        if vx == 0 and (x < xt[0] or x > xt[1]):
            # print(f"will not reach target vx == 0, x = {x}")
            break
        if y < yt[0]:
            # print(f"will not reach target y = {y} < yt {yt}")
            break
        if vx > 0:
            vx -= 1
        elif vx < 0:
            vx += 1
        vy -= 1

    if not hit_target:
        ymax = None

    return ymax, x, y, t


def read_groups(input_file, sep="\n"):
    with open(input_file, "r") as fn:
        buf = fn.read()
    return [e.strip() for e in buf.split(sep) if len(e.strip()) > 0]


def prep_data(input_file):
    import re
    grp = read_groups(input_file)
    print(grp[0])
    match = re.search(
        r"target area: x=([-\d]+)..([-\d]+), y=([-\d]+)..([-\d]+)", grp[0]
    )
    return tuple(int(k) for k in match.group(*range(1, 5)))


if __name__ == "__main__":

    valid_file = "data/17a.txt"
    input_file = "data/17.txt"

    # parts 1 and 2
    assert find_ymax(valid_file) == (45, 112)
    assert find_ymax(input_file) == (33670, 4903)
