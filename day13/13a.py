from Queue import Queue

def isWall(x, y):
    bin_value = bin(x * x + 3 * x + 2 * x * y + y + y * y + 1350)
    return bin_value.count('1') % 2 == 1 and x >= 0 and y >= 0

start = (1,1)
goal = (31,39)
frontier = Queue()
frontier.put(start)
came_from = {}
came_from[start] = None

while not frontier.empty():
    current = frontier.get()

    if current == goal:
        break

    for next in [(current[0] + 1, current[1]), (current[0] - 1, current[1]), (current[0], current[1] + 1), (current[0], current[1] - 1)]:
        if next not in came_from and not isWall(next[0], next[1]):
            frontier.put(next)
            came_from[next] = current
    

# Rebuild path
current = goal
path = [current]
while current != start:
    current = came_from[current]
    path.append(current)

print len(path) - 1