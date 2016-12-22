from collections import OrderedDict

with open('day22.txt', 'r') as f:
    lines = [x.strip().split() for x in f.readlines()]
lines = lines[2:]

nodes = OrderedDict()
for line in lines:
    _, x_string, y_string = line[0].split("-")
    coord = (int(x_string[1:]), int(y_string[1:]))
    size, used, available, usePercent = [int(x[:-1]) for x in line[1:]]
    nodes[coord] = (size, used, available, usePercent)

pairs = 0
for key1, value1 in nodes.items():
    for key2, value2 in nodes.items():
        pairs += value1 != value2 and value1[1] > 0 and value1[1] <= value2[2]

print pairs

