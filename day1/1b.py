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

def getCoordinate(bearing, coordinate):
    if bearing == 0:
        return (coordinate[0], coordinate[1] + 1)
    elif bearing == 90:
        return (coordinate[0] + 1, coordinate[1])
    elif bearing == 180:
        return (coordinate[0], coordinate[1] - 1)
    else:
        return (coordinate[0] - 1, coordinate[1])
        

# Read input
directions = []
with open('day1.txt', 'r') as inputfile:
    directions = inputfile.readline().split(',')

pointsVisited = set()
coordinate = (0,0)
bearing = 0
pointsVisited.add(coordinate)

# "Step" through directions (literally)
for d in directions:
    d = d.strip()
    #print d
    bearing = normalizeDirection(bearing, d[0])
    for i in range(0, int(d[1:])):
        coordinate = getCoordinate(bearing, coordinate)
        if coordinate not in pointsVisited:
            pointsVisited.add(coordinate)
        else:
            print abs(coordinate[0]) + abs(coordinate[1])
            quit()
    