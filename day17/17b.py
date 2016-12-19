from hashlib import md5
from itertools import compress
from Queue import Queue
from operator import add

# moves using array indexing [y][x]
moves = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1)
}

def getDoors(path):
    code = "awrkjxxr"
    hashValue =  md5(code + "".join(path)).hexdigest()
    return compress('UDLR', [x in "bcdef" for x in hashValue[:4]])

start = (0,0)
goal = (3,3)
frontier = Queue()
frontier.put((start, []))

paths = []
while not frontier.empty():
    currentPos, currentPath = frontier.get()
    if currentPos == goal:
        paths.append("".join(currentPath))
        continue
    for direction in getDoors(currentPath):   
        nextPos = tuple(map(add, currentPos, moves[direction]))
        if (0 <= nextPos[0] <= 3) and (0 <= nextPos[1] <= 3):
            frontier.put((nextPos, currentPath + [direction]))

print len(max(paths, key=len))