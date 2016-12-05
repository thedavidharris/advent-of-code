numpad = [[1,2,3],[4,5,6],[7,8,9]]
key = [1,1]
code = ""

def getNumber(line, key):
    for letter in line:
        if letter == "U":
            key[1] = max(0, key[1] - 1)
        elif letter == "D":
            key[1] = min(2, key[1] + 1)
        elif letter == "L":
            key[0] = max(0, key[0] - 1)
        elif letter == "R":
            key[0] = min(2, key[0] + 1)
    return key

# Parse input and get code
with open('day2.txt', 'r') as f:
    for line in f:
        key = getNumber(line, key)
        code += str(numpad[key[1]][key[0]])

print code