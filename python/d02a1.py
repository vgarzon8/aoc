# d02a1.py

input_file = "data/02.txt"

with open(input_file, "r") as fn:
    buf = fn.read()

dat = [e.strip().split() for e in buf.split('\n') if len(e.strip()) > 0]

print(dat[-5:])

x, y = 0, 0
for action, size in dat:
    size = int(size)
    if action == "forward":
        x += size
    elif action == "down":
        y += size
    elif action == "up":
        y -= size
    else:
        raise Exception("unrecognized action")

print(x, y, x * y)
# ans: 1924923
