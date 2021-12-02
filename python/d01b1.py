# d01b1.py
# Advent of Code 2021 day 1 part 2 ver 1
# count of rolling window increases
# input: https://adventofcode.com/2021/day/1/input

input_file = "data/01.txt"

with open(input_file, "r") as fn:
    buf = fn.read()

# buf = """199
# 200
# 208
# 210
# 200
# 207
# 240
# 269
# 260
# 263
# """

dat = [int(e.strip()) for e in buf.split('\n') if len(e) > 0]

win_sum = [sum(dat[slice(k, k + 3)]) for k in range(len(dat) - 2)]

incr = [win_sum[k + 1] > win_sum[k] for k in range(len(win_sum) - 1)]

print(sum(incr))

# ans: 1346
