with open('day20.txt', 'r') as f:
    input = f.readlines()
ranges = [map(int, x.strip().split("-")) for x in input]

sortedRanges = zip(sorted([column[0] for column in ranges]) + [2**32], [0] + sorted([column[1] for column in ranges]))

sum = 0
for low, high in sortedRanges:
    if low > high + 1:
        sum += low - high - 1

print sum