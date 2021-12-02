# d02b1.py

input_file = "data/02.txt"

with open(input_file, "r") as fn:
    buf = fn.read()

dat = [e.strip().split() for e in buf.split('\n') if len(e.strip()) > 0]

x, y, aim = 0, 0, 0
for action, size in dat:
    size = int(size)
    if action == "forward":
        x += size
        y += aim * size
    elif action == "down":
        aim += size
    elif action == "up":
        aim -= size
    else:
        raise Exception("unrecognized action")

print(x, y, aim, x * y)
# ans: 1982495697
