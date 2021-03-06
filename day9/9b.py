import re

def decompress(s):
    closure = re.search(r"\((\d+)x(\d+)\)", s)
    if closure:
        repeatLength = int(closure.group(1))
        repeatTimes = int(closure.group(2))
        firstPart = closure.start() + len(closure.group())
        recursiveLength = decompress(s[firstPart:firstPart+repeatLength])
        return len(s[:closure.start()]) + repeatTimes*recursiveLength + decompress(s[firstPart+repeatLength:])
    else:
        return len(s)

with open('day9.txt', 'r') as f:
    message = f.readline().strip()

print(decompress(message))