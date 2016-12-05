import csv

# Count number of "squares" traveled in each direction
directionCount = {
    "0": 0,
    "90": 0,
    "180": 0,
    "270": 0
}

# Normalize the direction facing
def normalizeDirection(bearing, direction):
    if direction == "L":
        return (bearing - 90) % 360
    else:
        return (bearing + 90) % 360

# Read input
directions = []
with open('day1.txt', 'r') as inputfile:
    directions = inputfile.readline().split(',')

bearing = 0

# "Step" through directions (literally)
count = 0
for d in directions:
    d = d.strip()
    bearing = normalizeDirection(bearing, d[0])
    directionCount[str(bearing)] += int(d[1:])

taxicabDistance = abs(directionCount["0"] - directionCount["180"]) + abs(directionCount["90"] - directionCount["270"])
print taxicabDistance