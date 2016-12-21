with open('day20.txt', 'r') as f:
    ranges = [map(int, x.strip().split("-")) for x in f.readlines()]
print filter(lambda range: range[0] > range[1] + 1, zip(sorted([column[0] for column in ranges]) + [2**32], [0] + sorted([column[1] for column in ranges])))[0][1] + 1