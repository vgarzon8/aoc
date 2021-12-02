# d01a1.py
# Advent of Code 2021 day 1 part 1 ver 1
# count of sequence increases
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

print(len(dat))
print(dat[:4])
print(dat[-4:])

incr = [dat[k + 1] > dat[k] for k in range(len(dat) - 1)]

print(len(incr))
print(incr[:3])
print(incr[-3:])

print(sum(incr))
# ans: 1301
