import re

def dragon_curve(x):
    y = "".join("1" if a=="0" else "0" for a in x[::-1])
    return x + "0" + y

def checksum(s):
    value = ""
    pairs = re.findall("..", s)
    for pair in pairs:
        value += str(int(pair[0] == pair[1]))
    if len(value) % 2 != 0:
        return value
    else:
        return checksum(value)

with open('day16.txt', 'r') as f:
    data = f.readline()

discLength = 272
while len(data) < discLength:
    data = dragon_curve(data)

data = data[:discLength]

checksumValue = checksum(data)
print checksumValue

