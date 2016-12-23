from collections import OrderedDict, namedtuple

with open('day22.txt', 'r') as f:
    lines = [x.strip().split() for x in f.readlines()]
lines = lines[2:]

nodes = OrderedDict()
Node = namedtuple('Node', 'size used available usePercent')
for line in lines:
    _, x_string, y_string = line[0].split("-")
    coord = (int(x_string[1:]), int(y_string[1:]))
    size, used, available, usePercent = [int(x[:-1]) for x in line[1:]]
    nodes[coord] = Node(size, used, available, usePercent)

pairs = 0
for key1, value1 in nodes.items():
    for key2, value2 in nodes.items():
        pairs += value1 != value2 and value1.used > 0 and value1.used <= value2.available

print pairs

