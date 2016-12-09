import numpy

with open('day8.txt', 'r') as f:
    text = f.readlines()

pixelCount = 0
for line in text:
    if line.startswith("rect"):
        locale = map(int, line.strip().split()[1].split("x"))
        pixelCount += reduce(lambda x, y: x*y, locale)

print(pixelCount)