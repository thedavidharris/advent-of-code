from collections import Counter

# Get input
with open('day6.txt', 'r') as f:
    input = f.read().strip()

print(''.join(Counter(x).most_common()[0][0] for x in zip(*input.splitlines())))
