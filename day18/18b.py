with open('day18.txt', 'r') as f:
    input = f.readline()

row = [x == "." for x in input]
numSafe = sum(row)
for _ in range (1, 400000):
    row = [True] + row + [True]
    row = [left == right for left, right in zip(row, row[2:])]
    numSafe += sum(row)
print numSafe