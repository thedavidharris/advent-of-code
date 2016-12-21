with open('day20.txt', 'r') as f:
    input = f.readlines()
ranges = [map(int, x.strip().split("-")) for x in input]

sortedRanges = zip(sorted([column[0] for column in ranges]) + [2**32], [0] + sorted([column[1] for column in ranges]))

min = 2**32
for low, high in sortedRanges:
    if low > high + 1:
        min = high + 1
        break

print min