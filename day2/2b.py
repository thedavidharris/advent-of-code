numpad = [
    [None, None, "1", None, None],
    [None, "2", "3", "4", None],
    ["5", "6", "7", "8", "9"],
    [None, "A", "B", "C", None],
    [None, None, "D", None, None]]
key = [2,0]
code = ""

def getNumber(line, key):
    for letter in line:
        x = key[0]
        y = key[1]
        if letter == "U":
            y = max(0, y - 1)
        if letter == "D":
            y = min(4, y + 1)
        if letter == "L":
            x = max(0, x - 1)
        if letter == "R":
            x = min(4, x + 1)
        if numpad[y][x] is not None:
            key[0] = x
            key[1] = y
    return key

# Parse input and get code
with open('day2.txt', 'r') as f:
    for line in f:
        key = getNumber(line, key)
        code += str(numpad[key[1]][key[0]])

print code