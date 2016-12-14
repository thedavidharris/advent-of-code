from Queue import Queue

def isWall(x, y):
    bin_value = bin(x * x + 3 * x + 2 * x * y + y + y * y + 1350)
    return bin_value.count('1') % 2 == 1 or x < 0 or y < 0

start = (1,1)
goal = (31,39)
frontier = Queue()
frontier.put(start)
distance = {}
distance[start] = 0
steps = 0

while not frontier.empty():
    current = frontier.get()

    for next in [(current[0] + 1, current[1]), (current[0] - 1, current[1]), (current[0], current[1] + 1), (current[0], current[1] - 1)]:
        if next not in distance and not isWall(next[0], next[1]):
            if distance[current] + 1 <= 50:
                frontier.put(next)
                distance[next] = distance[current] + 1

print len(distance)