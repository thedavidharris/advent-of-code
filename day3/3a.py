# Parse input and do stuff
with open('day3.txt', 'r') as f:
    numPossible = 0
    for line in f:
        a, b, c = [int(i) for i in line.split()]
        numPossible += 2 * max(a, b, c) < a + b + c
    print numPossible